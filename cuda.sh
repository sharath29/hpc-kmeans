python plot_in.py
nvcc gpu_kmeans.cu -o gpu_kmeans --compiler-options -ansi --compiler-options -Wall
./gpu_kmeans
python plot_out.py