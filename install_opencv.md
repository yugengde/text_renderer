```html


```
```
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential cmake unzip pkg-config
sudo apt-get install libjpeg-dev libtiff-dev libpng-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libopenblas-dev libatlas-base-dev gfortran
sudo apt-get install linux-image-generic linux-image-extra-virtual
sudo apt-get install linux-source linux-headers-generic
sudo apt-get install libhdf5-serial-dev
sudo apt-get install git
sudo apt-get install python3-dev
sudo apt install python3-widgetsnbextension
sudo apt install python3-testresources


pip3 install numpy
pip3 install scipy
pip3 install scikit-learn
pip3 install pillow
pip3 install h5py
sudo apt install g++-4.8

wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.1.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip
unzip opencv.zip
unzip opencv_contrib.zip

cd opencv-3.4.1/
mkdir build
cd build/

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_CUDA=ON -D CMAKE_C_COMPILER=gcc-4.8 -DCMAKE_CXX_COMPILER=g++-4.8 -D ENABLE_FAST_MATH=1 -D CUDA_FAST_MATH=1 -D WITH_CUBLAS=1 -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.1/modules -D BUILD_EXAMPLES=ON -D ENABLE_PRECOMPILED_HEADERS=OFF -DBUILD_opencv_cudacodec=OFF ..
make -j8
sudo make install

pip3 install cython

```


[安装参考地址](https://vlearningit.wordpress.com/install-nvidia-cuda-and-build-opencv-3-in-ubuntu-18-04-lts/)
