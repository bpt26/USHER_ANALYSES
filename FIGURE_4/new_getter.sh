
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_1.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_1.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_1.new.vcf.gz
usher --tree pruned_10_1.new.nh --vcf pruned_10_1.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_1.new.pb
usher --vcf missing_10_1.new.vcf.gz --load-assignments pruned_10_1.new.pb --print_uncondensed-final-tree 2> 1.log | tail -n 1 > usher_pruned_10_1.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_2.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_2.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_2.new.vcf.gz
usher --tree pruned_10_2.new.nh --vcf pruned_10_2.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_2.new.pb
usher --vcf missing_10_2.new.vcf.gz --load-assignments pruned_10_2.new.pb --print_uncondensed-final-tree 2> 2.log | tail -n 1 > usher_pruned_10_2.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_3.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_3.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_3.new.vcf.gz
usher --tree pruned_10_3.new.nh --vcf pruned_10_3.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_3.new.pb
usher --vcf missing_10_3.new.vcf.gz --load-assignments pruned_10_3.new.pb --print_uncondensed-final-tree 2> 3.log | tail -n 1 > usher_pruned_10_3.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_4.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_4.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_4.new.vcf.gz
usher --tree pruned_10_4.new.nh --vcf pruned_10_4.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_4.new.pb
usher --vcf missing_10_4.new.vcf.gz --load-assignments pruned_10_4.new.pb --print_uncondensed-final-tree 2> 4.log | tail -n 1 > usher_pruned_10_4.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_5.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_5.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_5.new.vcf.gz
usher --tree pruned_10_5.new.nh --vcf pruned_10_5.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_5.new.pb
usher --vcf missing_10_5.new.vcf.gz --load-assignments pruned_10_5.new.pb --print_uncondensed-final-tree 2> 5.log | tail -n 1 > usher_pruned_10_5.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_6.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_6.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_6.new.vcf.gz
usher --tree pruned_10_6.new.nh --vcf pruned_10_6.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_6.new.pb
usher --vcf missing_10_6.new.vcf.gz --load-assignments pruned_10_6.new.pb --print_uncondensed-final-tree 2> 6.log | tail -n 1 > usher_pruned_10_6.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_7.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_7.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_7.new.vcf.gz
usher --tree pruned_10_7.new.nh --vcf pruned_10_7.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_7.new.pb
usher --vcf missing_10_7.new.vcf.gz --load-assignments pruned_10_7.new.pb --print_uncondensed-final-tree 2> 7.log | tail -n 1 > usher_pruned_10_7.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_8.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_8.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_8.new.vcf.gz
usher --tree pruned_10_8.new.nh --vcf pruned_10_8.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_8.new.pb
usher --vcf missing_10_8.new.vcf.gz --load-assignments pruned_10_8.new.pb --print_uncondensed-final-tree 2> 8.log | tail -n 1 > usher_pruned_10_8.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_9.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_9.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_9.new.vcf.gz
usher --tree pruned_10_9.new.nh --vcf pruned_10_9.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_9.new.pb
usher --vcf missing_10_9.new.vcf.gz --load-assignments pruned_10_9.new.pb --print_uncondensed-final-tree 2> 9.log | tail -n 1 > usher_pruned_10_9.new.nh


wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_10.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_10.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_10.new.vcf.gz
usher --tree pruned_10_10.new.nh --vcf pruned_10_10.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_10.new.pb
usher --vcf missing_10_10.new.vcf.gz --load-assignments pruned_10_10.new.pb --print_uncondensed-final-tree 2> 10.log | tail -n 1 > usher_pruned_10_10.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_11.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_11.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_11.new.vcf.gz
usher --tree pruned_10_11.new.nh --vcf pruned_10_11.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_11.new.pb
usher --vcf missing_10_11.new.vcf.gz --load-assignments pruned_10_11.new.pb --print_uncondensed-final-tree 2> 11.log | tail -n 1 > usher_pruned_10_11.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_12.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_12.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_12.new.vcf.gz
usher --tree pruned_10_12.new.nh --vcf pruned_10_12.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_12.new.pb
usher --vcf missing_10_12.new.vcf.gz --load-assignments pruned_10_12.new.pb --print_uncondensed-final-tree 2> 12.log | tail -n 1 > usher_pruned_10_12.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_13.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_13.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_13.new.vcf.gz
usher --tree pruned_10_13.new.nh --vcf pruned_10_13.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_13.new.pb
usher --vcf missing_10_13.new.vcf.gz --load-assignments pruned_10_13.new.pb --print_uncondensed-final-tree 2> 13.log | tail -n 1 > usher_pruned_10_13.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_14.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_14.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_14.new.vcf.gz
usher --tree pruned_10_14.new.nh --vcf pruned_10_14.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_14.new.pb
usher --vcf missing_10_14.new.vcf.gz --load-assignments pruned_10_14.new.pb --print_uncondensed-final-tree 2> 14.log | tail -n 1 > usher_pruned_10_14.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_15.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_15.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_15.new.vcf.gz
usher --tree pruned_10_15.new.nh --vcf pruned_10_15.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_15.new.pb
usher --vcf missing_10_15.new.vcf.gz --load-assignments pruned_10_15.new.pb --print_uncondensed-final-tree 2> 15.log | tail -n 1 > usher_pruned_10_15.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_16.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_16.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_16.new.vcf.gz
usher --tree pruned_10_16.new.nh --vcf pruned_10_16.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_16.new.pb
usher --vcf missing_10_16.new.vcf.gz --load-assignments pruned_10_16.new.pb --print_uncondensed-final-tree 2> 16.log | tail -n 1 > usher_pruned_10_16.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_17.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_17.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_17.new.vcf.gz
usher --tree pruned_10_17.new.nh --vcf pruned_10_17.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_17.new.pb
usher --vcf missing_10_17.new.vcf.gz --load-assignments pruned_10_17.new.pb --print_uncondensed-final-tree 2> 17.log | tail -n 1 > usher_pruned_10_17.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_18.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_18.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_18.new.vcf.gz
usher --tree pruned_10_18.new.nh --vcf pruned_10_18.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_18.new.pb
usher --vcf missing_10_18.new.vcf.gz --load-assignments pruned_10_18.new.pb --print_uncondensed-final-tree 2> 18.log | tail -n 1 > usher_pruned_10_18.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_19.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_19.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_19.new.vcf.gz
usher --tree pruned_10_19.new.nh --vcf pruned_10_19.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_19.new.pb
usher --vcf missing_10_19.new.vcf.gz --load-assignments pruned_10_19.new.pb --print_uncondensed-final-tree 2> 19.log | tail -n 1 > usher_pruned_10_19.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_20.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_20.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_20.new.vcf.gz
usher --tree pruned_10_20.new.nh --vcf pruned_10_20.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_20.new.pb
usher --vcf missing_10_20.new.vcf.gz --load-assignments pruned_10_20.new.pb --print_uncondensed-final-tree 2> 20.log | tail -n 1 > usher_pruned_10_20.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_21.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_21.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_21.new.vcf.gz
usher --tree pruned_10_21.new.nh --vcf pruned_10_21.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_21.new.pb
usher --vcf missing_10_21.new.vcf.gz --load-assignments pruned_10_21.new.pb --print_uncondensed-final-tree 2> 21.log | tail -n 1 > usher_pruned_10_21.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_22.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_22.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_22.new.vcf.gz
usher --tree pruned_10_22.new.nh --vcf pruned_10_22.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_22.new.pb
usher --vcf missing_10_22.new.vcf.gz --load-assignments pruned_10_22.new.pb --print_uncondensed-final-tree 2> 22.log | tail -n 1 > usher_pruned_10_22.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_23.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_23.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_23.new.vcf.gz
usher --tree pruned_10_23.new.nh --vcf pruned_10_23.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_23.new.pb
usher --vcf missing_10_23.new.vcf.gz --load-assignments pruned_10_23.new.pb --print_uncondensed-final-tree 2> 23.log | tail -n 1 > usher_pruned_10_23.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_24.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_24.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_24.new.vcf.gz
usher --tree pruned_10_24.new.nh --vcf pruned_10_24.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_24.new.pb
usher --vcf missing_10_24.new.vcf.gz --load-assignments pruned_10_24.new.pb --print_uncondensed-final-tree 2> 24.log | tail -n 1 > usher_pruned_10_24.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_25.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_25.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_25.new.vcf.gz
usher --tree pruned_10_25.new.nh --vcf pruned_10_25.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_25.new.pb
usher --vcf missing_10_25.new.vcf.gz --load-assignments pruned_10_25.new.pb --print_uncondensed-final-tree 2> 25.log | tail -n 1 > usher_pruned_10_25.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_26.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_26.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_26.new.vcf.gz
usher --tree pruned_10_26.new.nh --vcf pruned_10_26.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_26.new.pb
usher --vcf missing_10_26.new.vcf.gz --load-assignments pruned_10_26.new.pb --print_uncondensed-final-tree 2> 26.log | tail -n 1 > usher_pruned_10_26.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_27.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_27.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_27.new.vcf.gz
usher --tree pruned_10_27.new.nh --vcf pruned_10_27.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_27.new.pb
usher --vcf missing_10_27.new.vcf.gz --load-assignments pruned_10_27.new.pb --print_uncondensed-final-tree 2> 27.log | tail -n 1 > usher_pruned_10_27.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_28.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_28.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_28.new.vcf.gz
usher --tree pruned_10_28.new.nh --vcf pruned_10_28.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_28.new.pb
usher --vcf missing_10_28.new.vcf.gz --load-assignments pruned_10_28.new.pb --print_uncondensed-final-tree 2> 28.log | tail -n 1 > usher_pruned_10_28.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_29.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_29.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_29.new.vcf.gz
usher --tree pruned_10_29.new.nh --vcf pruned_10_29.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_29.new.pb
usher --vcf missing_10_29.new.vcf.gz --load-assignments pruned_10_29.new.pb --print_uncondensed-final-tree 2> 29.log | tail -n 1 > usher_pruned_10_29.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_30.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_30.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_30.new.vcf.gz
usher --tree pruned_10_30.new.nh --vcf pruned_10_30.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_30.new.pb
usher --vcf missing_10_30.new.vcf.gz --load-assignments pruned_10_30.new.pb --print_uncondensed-final-tree 2> 30.log | tail -n 1 > usher_pruned_10_30.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_31.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_31.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_31.new.vcf.gz
usher --tree pruned_10_31.new.nh --vcf pruned_10_31.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_31.new.pb
usher --vcf missing_10_31.new.vcf.gz --load-assignments pruned_10_31.new.pb --print_uncondensed-final-tree 2> 31.log | tail -n 1 > usher_pruned_10_31.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_32.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_32.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_32.new.vcf.gz
usher --tree pruned_10_32.new.nh --vcf pruned_10_32.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_32.new.pb
usher --vcf missing_10_32.new.vcf.gz --load-assignments pruned_10_32.new.pb --print_uncondensed-final-tree 2> 32.log | tail -n 1 > usher_pruned_10_32.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_33.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_33.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_33.new.vcf.gz
usher --tree pruned_10_33.new.nh --vcf pruned_10_33.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_33.new.pb
usher --vcf missing_10_33.new.vcf.gz --load-assignments pruned_10_33.new.pb --print_uncondensed-final-tree 2> 33.log | tail -n 1 > usher_pruned_10_33.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_34.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_34.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_34.new.vcf.gz
usher --tree pruned_10_34.new.nh --vcf pruned_10_34.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_34.new.pb
usher --vcf missing_10_34.new.vcf.gz --load-assignments pruned_10_34.new.pb --print_uncondensed-final-tree 2> 34.log | tail -n 1 > usher_pruned_10_34.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_35.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_35.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_35.new.vcf.gz
usher --tree pruned_10_35.new.nh --vcf pruned_10_35.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_35.new.pb
usher --vcf missing_10_35.new.vcf.gz --load-assignments pruned_10_35.new.pb --print_uncondensed-final-tree 2> 35.log | tail -n 1 > usher_pruned_10_35.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_36.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_36.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_36.new.vcf.gz
usher --tree pruned_10_36.new.nh --vcf pruned_10_36.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_36.new.pb
usher --vcf missing_10_36.new.vcf.gz --load-assignments pruned_10_36.new.pb --print_uncondensed-final-tree 2> 36.log | tail -n 1 > usher_pruned_10_36.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_37.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_37.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_37.new.vcf.gz
usher --tree pruned_10_37.new.nh --vcf pruned_10_37.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_37.new.pb
usher --vcf missing_10_37.new.vcf.gz --load-assignments pruned_10_37.new.pb --print_uncondensed-final-tree 2> 37.log | tail -n 1 > usher_pruned_10_37.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_38.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_38.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_38.new.vcf.gz
usher --tree pruned_10_38.new.nh --vcf pruned_10_38.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_38.new.pb
usher --vcf missing_10_38.new.vcf.gz --load-assignments pruned_10_38.new.pb --print_uncondensed-final-tree 2> 38.log | tail -n 1 > usher_pruned_10_38.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_39.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_39.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_39.new.vcf.gz
usher --tree pruned_10_39.new.nh --vcf pruned_10_39.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_39.new.pb
usher --vcf missing_10_39.new.vcf.gz --load-assignments pruned_10_39.new.pb --print_uncondensed-final-tree 2> 39.log | tail -n 1 > usher_pruned_10_39.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_40.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_40.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_40.new.vcf.gz
usher --tree pruned_10_40.new.nh --vcf pruned_10_40.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_40.new.pb
usher --vcf missing_10_40.new.vcf.gz --load-assignments pruned_10_40.new.pb --print_uncondensed-final-tree 2> 40.log | tail -n 1 > usher_pruned_10_40.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_41.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_41.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_41.new.vcf.gz
usher --tree pruned_10_41.new.nh --vcf pruned_10_41.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_41.new.pb
usher --vcf missing_10_41.new.vcf.gz --load-assignments pruned_10_41.new.pb --print_uncondensed-final-tree 2> 41.log | tail -n 1 > usher_pruned_10_41.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_42.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_42.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_42.new.vcf.gz
usher --tree pruned_10_42.new.nh --vcf pruned_10_42.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_42.new.pb
usher --vcf missing_10_42.new.vcf.gz --load-assignments pruned_10_42.new.pb --print_uncondensed-final-tree 2> 42.log | tail -n 1 > usher_pruned_10_42.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_43.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_43.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_43.new.vcf.gz
usher --tree pruned_10_43.new.nh --vcf pruned_10_43.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_43.new.pb
usher --vcf missing_10_43.new.vcf.gz --load-assignments pruned_10_43.new.pb --print_uncondensed-final-tree 2> 43.log | tail -n 1 > usher_pruned_10_43.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_44.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_44.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_44.new.vcf.gz
usher --tree pruned_10_44.new.nh --vcf pruned_10_44.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_44.new.pb
usher --vcf missing_10_44.new.vcf.gz --load-assignments pruned_10_44.new.pb --print_uncondensed-final-tree 2> 44.log | tail -n 1 > usher_pruned_10_44.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_45.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_45.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_45.new.vcf.gz
usher --tree pruned_10_45.new.nh --vcf pruned_10_45.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_45.new.pb
usher --vcf missing_10_45.new.vcf.gz --load-assignments pruned_10_45.new.pb --print_uncondensed-final-tree 2> 45.log | tail -n 1 > usher_pruned_10_45.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_46.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_46.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_46.new.vcf.gz
usher --tree pruned_10_46.new.nh --vcf pruned_10_46.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_46.new.pb
usher --vcf missing_10_46.new.vcf.gz --load-assignments pruned_10_46.new.pb --print_uncondensed-final-tree 2> 46.log | tail -n 1 > usher_pruned_10_46.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_47.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_47.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_47.new.vcf.gz
usher --tree pruned_10_47.new.nh --vcf pruned_10_47.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_47.new.pb
usher --vcf missing_10_47.new.vcf.gz --load-assignments pruned_10_47.new.pb --print_uncondensed-final-tree 2> 47.log | tail -n 1 > usher_pruned_10_47.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_48.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_48.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_48.new.vcf.gz
usher --tree pruned_10_48.new.nh --vcf pruned_10_48.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_48.new.pb
usher --vcf missing_10_48.new.vcf.gz --load-assignments pruned_10_48.new.pb --print_uncondensed-final-tree 2> 48.log | tail -n 1 > usher_pruned_10_48.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_49.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_49.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_49.new.vcf.gz
usher --tree pruned_10_49.new.nh --vcf pruned_10_49.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_49.new.pb
usher --vcf missing_10_49.new.vcf.gz --load-assignments pruned_10_49.new.pb --print_uncondensed-final-tree 2> 49.log | tail -n 1 > usher_pruned_10_49.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_50.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_50.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_50.new.vcf.gz
usher --tree pruned_10_50.new.nh --vcf pruned_10_50.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_50.new.pb
usher --vcf missing_10_50.new.vcf.gz --load-assignments pruned_10_50.new.pb --print_uncondensed-final-tree 2> 50.log | tail -n 1 > usher_pruned_10_50.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_51.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_51.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_51.new.vcf.gz
usher --tree pruned_10_51.new.nh --vcf pruned_10_51.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_51.new.pb
usher --vcf missing_10_51.new.vcf.gz --load-assignments pruned_10_51.new.pb --print_uncondensed-final-tree 2> 51.log | tail -n 1 > usher_pruned_10_51.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_52.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_52.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_52.new.vcf.gz
usher --tree pruned_10_52.new.nh --vcf pruned_10_52.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_52.new.pb
usher --vcf missing_10_52.new.vcf.gz --load-assignments pruned_10_52.new.pb --print_uncondensed-final-tree 2> 52.log | tail -n 1 > usher_pruned_10_52.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_53.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_53.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_53.new.vcf.gz
usher --tree pruned_10_53.new.nh --vcf pruned_10_53.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_53.new.pb
usher --vcf missing_10_53.new.vcf.gz --load-assignments pruned_10_53.new.pb --print_uncondensed-final-tree 2> 53.log | tail -n 1 > usher_pruned_10_53.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_54.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_54.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_54.new.vcf.gz
usher --tree pruned_10_54.new.nh --vcf pruned_10_54.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_54.new.pb
usher --vcf missing_10_54.new.vcf.gz --load-assignments pruned_10_54.new.pb --print_uncondensed-final-tree 2> 54.log | tail -n 1 > usher_pruned_10_54.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_55.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_55.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_55.new.vcf.gz
usher --tree pruned_10_55.new.nh --vcf pruned_10_55.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_55.new.pb
usher --vcf missing_10_55.new.vcf.gz --load-assignments pruned_10_55.new.pb --print_uncondensed-final-tree 2> 55.log | tail -n 1 > usher_pruned_10_55.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_56.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_56.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_56.new.vcf.gz
usher --tree pruned_10_56.new.nh --vcf pruned_10_56.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_56.new.pb
usher --vcf missing_10_56.new.vcf.gz --load-assignments pruned_10_56.new.pb --print_uncondensed-final-tree 2> 56.log | tail -n 1 > usher_pruned_10_56.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_57.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_57.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_57.new.vcf.gz
usher --tree pruned_10_57.new.nh --vcf pruned_10_57.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_57.new.pb
usher --vcf missing_10_57.new.vcf.gz --load-assignments pruned_10_57.new.pb --print_uncondensed-final-tree 2> 57.log | tail -n 1 > usher_pruned_10_57.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_58.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_58.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_58.new.vcf.gz
usher --tree pruned_10_58.new.nh --vcf pruned_10_58.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_58.new.pb
usher --vcf missing_10_58.new.vcf.gz --load-assignments pruned_10_58.new.pb --print_uncondensed-final-tree 2> 58.log | tail -n 1 > usher_pruned_10_58.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_59.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_59.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_59.new.vcf.gz
usher --tree pruned_10_59.new.nh --vcf pruned_10_59.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_59.new.pb
usher --vcf missing_10_59.new.vcf.gz --load-assignments pruned_10_59.new.pb --print_uncondensed-final-tree 2> 59.log | tail -n 1 > usher_pruned_10_59.new.nh


wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_60.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_60.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_60.new.vcf.gz
usher --tree pruned_10_60.new.nh --vcf pruned_10_60.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_60.new.pb
usher --vcf missing_10_60.new.vcf.gz --load-assignments pruned_10_60.new.pb --print_uncondensed-final-tree 2> 60.log | tail -n 1 > usher_pruned_10_60.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_61.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_61.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_61.new.vcf.gz
usher --tree pruned_10_61.new.nh --vcf pruned_10_61.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_61.new.pb
usher --vcf missing_10_61.new.vcf.gz --load-assignments pruned_10_61.new.pb --print_uncondensed-final-tree 2> 61.log | tail -n 1 > usher_pruned_10_61.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_62.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_62.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_62.new.vcf.gz
usher --tree pruned_10_62.new.nh --vcf pruned_10_62.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_62.new.pb
usher --vcf missing_10_62.new.vcf.gz --load-assignments pruned_10_62.new.pb --print_uncondensed-final-tree 2> 62.log | tail -n 1 > usher_pruned_10_62.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_63.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_63.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_63.new.vcf.gz
usher --tree pruned_10_63.new.nh --vcf pruned_10_63.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_63.new.pb
usher --vcf missing_10_63.new.vcf.gz --load-assignments pruned_10_63.new.pb --print_uncondensed-final-tree 2> 63.log | tail -n 1 > usher_pruned_10_63.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_64.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_64.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_64.new.vcf.gz
usher --tree pruned_10_64.new.nh --vcf pruned_10_64.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_64.new.pb
usher --vcf missing_10_64.new.vcf.gz --load-assignments pruned_10_64.new.pb --print_uncondensed-final-tree 2> 64.log | tail -n 1 > usher_pruned_10_64.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_65.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_65.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_65.new.vcf.gz
usher --tree pruned_10_65.new.nh --vcf pruned_10_65.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_65.new.pb
usher --vcf missing_10_65.new.vcf.gz --load-assignments pruned_10_65.new.pb --print_uncondensed-final-tree 2> 65.log | tail -n 1 > usher_pruned_10_65.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_66.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_66.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_66.new.vcf.gz
usher --tree pruned_10_66.new.nh --vcf pruned_10_66.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_66.new.pb
usher --vcf missing_10_66.new.vcf.gz --load-assignments pruned_10_66.new.pb --print_uncondensed-final-tree 2> 66.log | tail -n 1 > usher_pruned_10_66.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_67.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_67.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_67.new.vcf.gz
usher --tree pruned_10_67.new.nh --vcf pruned_10_67.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_67.new.pb
usher --vcf missing_10_67.new.vcf.gz --load-assignments pruned_10_67.new.pb --print_uncondensed-final-tree 2> 67.log | tail -n 1 > usher_pruned_10_67.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_68.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_68.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_68.new.vcf.gz
usher --tree pruned_10_68.new.nh --vcf pruned_10_68.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_68.new.pb
usher --vcf missing_10_68.new.vcf.gz --load-assignments pruned_10_68.new.pb --print_uncondensed-final-tree 2> 68.log | tail -n 1 > usher_pruned_10_68.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_69.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_69.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_69.new.vcf.gz
usher --tree pruned_10_69.new.nh --vcf pruned_10_69.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_69.new.pb
usher --vcf missing_10_69.new.vcf.gz --load-assignments pruned_10_69.new.pb --print_uncondensed-final-tree 2> 69.log | tail -n 1 > usher_pruned_10_69.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_70.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_70.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_70.new.vcf.gz
usher --tree pruned_10_70.new.nh --vcf pruned_10_70.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_70.new.pb
usher --vcf missing_10_70.new.vcf.gz --load-assignments pruned_10_70.new.pb --print_uncondensed-final-tree 2> 70.log | tail -n 1 > usher_pruned_10_70.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_71.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_71.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_71.new.vcf.gz
usher --tree pruned_10_71.new.nh --vcf pruned_10_71.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_71.new.pb
usher --vcf missing_10_71.new.vcf.gz --load-assignments pruned_10_71.new.pb --print_uncondensed-final-tree 2> 71.log | tail -n 1 > usher_pruned_10_71.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_72.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_72.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_72.new.vcf.gz
usher --tree pruned_10_72.new.nh --vcf pruned_10_72.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_72.new.pb
usher --vcf missing_10_72.new.vcf.gz --load-assignments pruned_10_72.new.pb --print_uncondensed-final-tree 2> 72.log | tail -n 1 > usher_pruned_10_72.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_73.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_73.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_73.new.vcf.gz
usher --tree pruned_10_73.new.nh --vcf pruned_10_73.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_73.new.pb
usher --vcf missing_10_73.new.vcf.gz --load-assignments pruned_10_73.new.pb --print_uncondensed-final-tree 2> 73.log | tail -n 1 > usher_pruned_10_73.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_74.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_74.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_74.new.vcf.gz
usher --tree pruned_10_74.new.nh --vcf pruned_10_74.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_74.new.pb
usher --vcf missing_10_74.new.vcf.gz --load-assignments pruned_10_74.new.pb --print_uncondensed-final-tree 2> 74.log | tail -n 1 > usher_pruned_10_74.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_75.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_75.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_75.new.vcf.gz
usher --tree pruned_10_75.new.nh --vcf pruned_10_75.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_75.new.pb
usher --vcf missing_10_75.new.vcf.gz --load-assignments pruned_10_75.new.pb --print_uncondensed-final-tree 2> 75.log | tail -n 1 > usher_pruned_10_75.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_76.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_76.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_76.new.vcf.gz
usher --tree pruned_10_76.new.nh --vcf pruned_10_76.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_76.new.pb
usher --vcf missing_10_76.new.vcf.gz --load-assignments pruned_10_76.new.pb --print_uncondensed-final-tree 2> 76.log | tail -n 1 > usher_pruned_10_76.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_77.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_77.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_77.new.vcf.gz
usher --tree pruned_10_77.new.nh --vcf pruned_10_77.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_77.new.pb
usher --vcf missing_10_77.new.vcf.gz --load-assignments pruned_10_77.new.pb --print_uncondensed-final-tree 2> 77.log | tail -n 1 > usher_pruned_10_77.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_78.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_78.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_78.new.vcf.gz
usher --tree pruned_10_78.new.nh --vcf pruned_10_78.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_78.new.pb
usher --vcf missing_10_78.new.vcf.gz --load-assignments pruned_10_78.new.pb --print_uncondensed-final-tree 2> 78.log | tail -n 1 > usher_pruned_10_78.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_79.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_79.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_79.new.vcf.gz
usher --tree pruned_10_79.new.nh --vcf pruned_10_79.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_79.new.pb
usher --vcf missing_10_79.new.vcf.gz --load-assignments pruned_10_79.new.pb --print_uncondensed-final-tree 2> 79.log | tail -n 1 > usher_pruned_10_79.new.nh


wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_80.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_80.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_80.new.vcf.gz
usher --tree pruned_10_80.new.nh --vcf pruned_10_80.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_80.new.pb
usher --vcf missing_10_80.new.vcf.gz --load-assignments pruned_10_80.new.pb --print_uncondensed-final-tree 2> 80.log | tail -n 1 > usher_pruned_10_80.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_81.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_81.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_81.new.vcf.gz
usher --tree pruned_10_81.new.nh --vcf pruned_10_81.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_81.new.pb
usher --vcf missing_10_81.new.vcf.gz --load-assignments pruned_10_81.new.pb --print_uncondensed-final-tree 2> 81.log | tail -n 1 > usher_pruned_10_81.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_82.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_82.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_82.new.vcf.gz
usher --tree pruned_10_82.new.nh --vcf pruned_10_82.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_82.new.pb
usher --vcf missing_10_82.new.vcf.gz --load-assignments pruned_10_82.new.pb --print_uncondensed-final-tree 2> 82.log | tail -n 1 > usher_pruned_10_82.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_83.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_83.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_83.new.vcf.gz
usher --tree pruned_10_83.new.nh --vcf pruned_10_83.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_83.new.pb
usher --vcf missing_10_83.new.vcf.gz --load-assignments pruned_10_83.new.pb --print_uncondensed-final-tree 2> 83.log | tail -n 1 > usher_pruned_10_83.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_84.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_84.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_84.new.vcf.gz
usher --tree pruned_10_84.new.nh --vcf pruned_10_84.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_84.new.pb
usher --vcf missing_10_84.new.vcf.gz --load-assignments pruned_10_84.new.pb --print_uncondensed-final-tree 2> 84.log | tail -n 1 > usher_pruned_10_84.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_85.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_85.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_85.new.vcf.gz
usher --tree pruned_10_85.new.nh --vcf pruned_10_85.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_85.new.pb
usher --vcf missing_10_85.new.vcf.gz --load-assignments pruned_10_85.new.pb --print_uncondensed-final-tree 2> 85.log | tail -n 1 > usher_pruned_10_85.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_86.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_86.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_86.new.vcf.gz
usher --tree pruned_10_86.new.nh --vcf pruned_10_86.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_86.new.pb
usher --vcf missing_10_86.new.vcf.gz --load-assignments pruned_10_86.new.pb --print_uncondensed-final-tree 2> 86.log | tail -n 1 > usher_pruned_10_86.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_87.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_87.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_87.new.vcf.gz
usher --tree pruned_10_87.new.nh --vcf pruned_10_87.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_87.new.pb
usher --vcf missing_10_87.new.vcf.gz --load-assignments pruned_10_87.new.pb --print_uncondensed-final-tree 2> 87.log | tail -n 1 > usher_pruned_10_87.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_88.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_88.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_88.new.vcf.gz
usher --tree pruned_10_88.new.nh --vcf pruned_10_88.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_88.new.pb
usher --vcf missing_10_88.new.vcf.gz --load-assignments pruned_10_88.new.pb --print_uncondensed-final-tree 2> 88.log | tail -n 1 > usher_pruned_10_88.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_89.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_89.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_89.new.vcf.gz
usher --tree pruned_10_89.new.nh --vcf pruned_10_89.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_89.new.pb
usher --vcf missing_10_89.new.vcf.gz --load-assignments pruned_10_89.new.pb --print_uncondensed-final-tree 2> 89.log | tail -n 1 > usher_pruned_10_89.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_90.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_90.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_90.new.vcf.gz
usher --tree pruned_10_90.new.nh --vcf pruned_10_90.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_90.new.pb
usher --vcf missing_10_90.new.vcf.gz --load-assignments pruned_10_90.new.pb --print_uncondensed-final-tree 2> 90.log | tail -n 1 > usher_pruned_10_90.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_91.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_91.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_91.new.vcf.gz
usher --tree pruned_10_91.new.nh --vcf pruned_10_91.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_91.new.pb
usher --vcf missing_10_91.new.vcf.gz --load-assignments pruned_10_91.new.pb --print_uncondensed-final-tree 2> 91.log | tail -n 1 > usher_pruned_10_91.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_92.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_92.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_92.new.vcf.gz
usher --tree pruned_10_92.new.nh --vcf pruned_10_92.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_92.new.pb
usher --vcf missing_10_92.new.vcf.gz --load-assignments pruned_10_92.new.pb --print_uncondensed-final-tree 2> 92.log | tail -n 1 > usher_pruned_10_92.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_93.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_93.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_93.new.vcf.gz
usher --tree pruned_10_93.new.nh --vcf pruned_10_93.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_93.new.pb
usher --vcf missing_10_93.new.vcf.gz --load-assignments pruned_10_93.new.pb --print_uncondensed-final-tree 2> 93.log | tail -n 1 > usher_pruned_10_93.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_94.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_94.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_94.new.vcf.gz
usher --tree pruned_10_94.new.nh --vcf pruned_10_94.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_94.new.pb
usher --vcf missing_10_94.new.vcf.gz --load-assignments pruned_10_94.new.pb --print_uncondensed-final-tree 2> 94.log | tail -n 1 > usher_pruned_10_94.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_95.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_95.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_95.new.vcf.gz
usher --tree pruned_10_95.new.nh --vcf pruned_10_95.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_95.new.pb
usher --vcf missing_10_95.new.vcf.gz --load-assignments pruned_10_95.new.pb --print_uncondensed-final-tree 2> 95.log | tail -n 1 > usher_pruned_10_95.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_96.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_96.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_96.new.vcf.gz
usher --tree pruned_10_96.new.nh --vcf pruned_10_96.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_96.new.pb
usher --vcf missing_10_96.new.vcf.gz --load-assignments pruned_10_96.new.pb --print_uncondensed-final-tree 2> 96.log | tail -n 1 > usher_pruned_10_96.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_97.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_97.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_97.new.vcf.gz
usher --tree pruned_10_97.new.nh --vcf pruned_10_97.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_97.new.pb
usher --vcf missing_10_97.new.vcf.gz --load-assignments pruned_10_97.new.pb --print_uncondensed-final-tree 2> 97.log | tail -n 1 > usher_pruned_10_97.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_98.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_98.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_98.new.vcf.gz
usher --tree pruned_10_98.new.nh --vcf pruned_10_98.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_98.new.pb
usher --vcf missing_10_98.new.vcf.gz --load-assignments pruned_10_98.new.pb --print_uncondensed-final-tree 2> 98.log | tail -n 1 > usher_pruned_10_98.new.nh

wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/missing_10_99.new.vcf.gz
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_99.new.nh
wget http://public.gi.ucsc.edu/~yatisht/data/pruning_experiments/real_data/pruned_10_99.new.vcf.gz
usher --tree pruned_10_99.new.nh --vcf pruned_10_99.new.vcf.gz --collapse-final-tree --save-assignments pruned_10_99.new.pb
usher --vcf missing_10_99.new.vcf.gz --load-assignments pruned_10_99.new.pb --print_uncondensed-final-tree 2> 99.log | tail -n 1 > usher_pruned_10_99.new.nh

