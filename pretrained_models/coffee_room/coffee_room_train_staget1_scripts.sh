# split 1
python run.py --use_cuda --save_args --step_size 800 \
            --dataset 'coffee_room' --split 1 \
            --split_segments \
            --use_pe_tgt \
            --do_framewise_loss --do_framewise_loss_g --framewise_loss_g_apply_nothing \
            --do_segwise_loss --do_segwise_loss_g --segwise_loss_g_apply_logsoftmax \
            --do_crossattention_action_loss_nll \
            --exp_name 'coffee_room1' \
            --data_root C:/Users/test/Desktop/Leon/Projects/MS-TCN2/data \
	    --seed 3672463022