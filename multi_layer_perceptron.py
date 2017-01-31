import datetime
import numpy as np
import tensorflow as tf

import os


TRAIN_DATA_PATH = './data/train/range_14_16_men/'
TEST_DATA_PATH = './data/test/range_14_16_men_test_data.csv'

#Parameters
learning_rate = 1e-3
batch_size = 800
display_step = 100
train_data_records = 1428368
training_epochs=2

# Network Parameters
num_features = 10
n_classes = 1
n_hidden_1 =  8
n_hidden_2 =  4


def read_my_file_format(filename_queue):
    reader = tf.TextLineReader(skip_header_lines=1,name='train_data')
    key, value = reader.read(filename_queue)


    record_defaults = [
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32),
        tf.constant([], dtype=tf.float32)
    ]

    Xi1, Xi2, Xi3, Xi4, Xi5, Xi6, Xi7, Xi8, Xi9, Xi10, Xo = \
        tf.decode_csv(value, record_defaults=record_defaults, field_delim=',')

    features = tf.pack([ Xi1, Xi2, Xi3, Xi4, Xi5, Xi6, Xi7, Xi8, Xi9, Xi10])
    label = tf.pack([ Xo])
    return features, label

def input_pipeline(filenames, batch_size, read_threads, num_epochs=None):
  filename_queue = tf.train.string_input_producer(
      filenames, num_epochs=num_epochs, shuffle=True)
  example_list = [read_my_file_format(filename_queue) for _ in range(read_threads)]
  min_after_dequeue = 10000
  capacity = min_after_dequeue + 3 * batch_size
  example_batch, label_batch = \
      tf.train.shuffle_batch_join(example_list, batch_size=batch_size, capacity=capacity,min_after_dequeue=min_after_dequeue)
  return example_batch, label_batch

def multilayer_perceptron(x, weights, biases):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['h1']), biases['b1']), name="layer_1")
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['h2']), biases['b2']), name="layer_2")
    out_layer = tf.matmul(layer_2, weights['out'])+ biases['out']
    return out_layer

def main():
    x = tf.placeholder(tf.float32, [None, num_features])
    y = tf.placeholder(tf.float32, [None, n_classes])
    weights = {
        'h1': tf.Variable(tf.random_normal([num_features, n_hidden_1]), dtype=tf.float32),
        'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2]), dtype=tf.float32),
        'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]), dtype=tf.float32)
    }
    biases = {
        'b1': tf.Variable(tf.ones([n_hidden_1]), dtype=tf.float32),
        'b2': tf.Variable(tf.ones([n_hidden_2]), dtype=tf.float32),
        'out': tf.Variable(tf.ones([n_classes]), dtype=tf.float32)
    }


    # Construct model
    pred = multilayer_perceptron(x,weights, biases)


    # Define cost and optimizer
    cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(pred, y))
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

    # Evaluate model
    correct_prediction = tf.equal(tf.round(tf.nn.sigmoid(pred)), tf.round(y))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


    train_data_files = [os.path.join(TRAIN_DATA_PATH, i) for i in os.listdir(TRAIN_DATA_PATH)]
    batch_x, batch_y = input_pipeline(train_data_files, batch_size, 10)

    # Timing
    startTime = datetime.datetime.now()

    # Initializing the variables
    init = tf.initialize_all_variables()
    with tf.Session() as sess:

        # Initialize the variables (like the epoch counter).
        sess.run(init)

        # Start input enqueue threads.
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        for epoch in range(training_epochs):
            avg_cost = 0
            total_batch = int(train_data_records / batch_size)
            print ("Total batch units ", total_batch)
            for i in range(total_batch):
                b_x, b_y = sess.run([batch_x, batch_y])
                _, c = sess.run([optimizer, cost], feed_dict={x: b_x, y: b_y})
                avg_cost += c / total_batch
                if i % display_step == 0:
                    _, c = sess.run([optimizer, cost], feed_dict={x: b_x, y: b_y})
                    print("Epoch: %03d/%03d, iteration %03d/%03d,   cost: %.9f" % (epoch+1, training_epochs,i,total_batch,avg_cost))
                    train_acc = sess.run(accuracy, feed_dict={x: b_x, y: b_y})
                    print(" Training accuracy: %.3f" % (train_acc))

            print("Epoch: %03d/%03d cost: %.9f" % (epoch+1, training_epochs, avg_cost))

        print("Training complete!")
        endTime = datetime.datetime.now()
        fitTime = (endTime - startTime)
        print("Training Time:", fitTime)

        coord.request_stop()

        # Wait for threads to finish.
        coord.join(threads)
        # Test model
        _, c = sess.run([optimizer, cost], feed_dict={x: b_x, y: b_y})
        print("Epoch: %03d/%03d, iteration %03d/%03d,   cost: %.9f" % (epoch, training_epochs, i, total_batch, avg_cost))
        train_acc = sess.run(accuracy, feed_dict={x: b_x, y: b_y})
        print(" Training accuracy: %.3f" % (train_acc))
        test_data = np.genfromtxt(TEST_DATA_PATH, delimiter=',')
        activation = tf.nn.sigmoid(pred, name="output")
        print("final accuracy is ", sess.run(activation, feed_dict={x: test_data[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], y: test_data[:, [10]]})*100,"%")
        sess.close()

def calculate(x):
    return round(x)

def print_result(test_data, prediction):
    success_predictions = 0
    for row in range(0, 9):
        print("Person ", row, " of ", 6)
        print(" Is short: ", test_data.item(row,0))
        print(" Shy: ", test_data.item(row, 1))
        print(" Wear braces: ", test_data.item(row, 2))
        print(" Wear glasses: ", test_data.item(row, 3))
        print(" Is less popular: ", test_data.item(row, 4))
        print(" Different race: ", test_data.item(row, 5))
        print(" Low socioeconomic status: ", test_data.item(row, 6))
        print(" Gay or lesbian: ", test_data.item(row, 7))
        print(" Have disability: ", test_data.item(row, 8))
        print(" Overweight: ", test_data.item(row, 9))
        print(" Suffer bullying: ", test_data.item(row, 10))
        print("-----------------")
        print(" Prediction: ", round((int)(prediction.item(row))))
        print("-----------------")
        if ((test_data.item(row, 10)) == (int)(prediction.item(row))):
            success_predictions+=1
    print("\n\n Success predictions ", success_predictions," of ",10)


if __name__ == "__main__":
    main()