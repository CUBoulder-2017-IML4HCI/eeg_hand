OSCproxy.py
GitHub Repo -- https://github.com/CUBoulder-2017-IML4HCI/eeg_hand

OSC proxy is a simple osc feature extractor. It takes OSC input, in my case from an eeg
headband, processes the data and takes the mean of 10 samples and forward to weki at a specified port.
In its current form, it takes the mean but this can be altered to do whatever preprocessing deemed
appropriate. Essentially, this program sits between the sensors and weki and allows preprocessing.

No compilation is necessary as this is a python program. To use the program set the output of
the whatever sensors desired to port 8200. Set weki to receive inputs on port 6448. The program will send
the mean of every 10 values to weki.
