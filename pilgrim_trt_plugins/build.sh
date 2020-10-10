mkdir build
cd build
cmake -DTENSORRT_DIR=~/TensorRT ..
make -j7
cd ..
P=`pwd`

echo 'Now pls add this variable to your ~/.bashrc or ~/.zshrc'
echo "echo 'export PILGRIM_TRT_PLUGINS_LIB=$P/build/lib' >> ~/.zshrc" 
