# Image to Text

Convert images into ascii art. This script has been tested with Python 2.7.

## Installation

Pip needs to be installed. On Ubuntu, this can be done by running this command:

```
sudo apt install -y python-pip
```

Update pip to the latest version:
```
sudo -H pip install -U pip --upgrade pip
```

Install setup-tools using pip:
```
sudo -H pip install -U pip setuptools
```

Install dependencies using setuptools:
```
sudo python setup.py install
```

## Requirements

This script requires:
+ Python 2.7
+ Pillow library

## Example usage

```
$ python img2text.py samples/bird.png --inverted
                                                             ▒▒
                                                           ░▓▓▓
                                                         ░▓▓▓▓▓
                                                       ░▓▓▓▓▓▓▒
                                                     ░▓▓▓▓▓▓▓▒░▒▒
                                                   ░▓▓▓▓▓▓▓▓▓▓▓▓▓
                                                 ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
                                               ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
                                             ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░
                                           ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
                                         ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
                                       ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
                                     ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
                                   ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
             ░░▒▒▒▒▒░░            ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
           ░▒▒▒▒▒▒▒▒▒▒▒▒▒░      ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
          ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░  ▒▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░
          ▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░
         ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░
          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░
          ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░
            ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░
             ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒
               ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
               ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░
                ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░
                 ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░ ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
                  ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░ ░░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▒░░
                   ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒░░ ░░░
                    ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒░
                     ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░
                       ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
                         ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▓▓▒▒▒░░
                           ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░       ░▓▓▓▒▒▒░░
                               ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░             ░▒▓▓▓▒▒▒▒░
                                                                  ▒▓▓▓▓▒▒▒▒░░
                                                                   ░▓▓▓▓▒▒▒▒▒░░
                                                                     ▒▓▓▓▓▒▒▒▒▒▒░
                                                                      ░▓▓▓▓▓▒▒▒▒▒▒░░
                                                                       ░▒▓▓▓▓▓▒▒▒▒▒▒
                                                                         ▒▓▓▓▓▓▒░
                                                                          ░░▒▓▓▓▒


```