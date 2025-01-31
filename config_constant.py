
default_dict = dict(out_dir='outputs', trainer='WeightedProcrustesTrainer', batch_size=4, val_batch_size=1, train_phase='train', val_phase='val', test_phase='test', use_random_scale=False, min_scale=0.8, max_scale=1.2, use_random_rotation=True, rotation_range=360, positive_pair_search_voxel_size_multiplier=1.5, save_epoch_freq=1, val_epoch_freq=1, stat_freq=40, test_valid=True, val_max_iter=400, use_balanced_loss=False, inlier_direct_loss_weight=1.0, procrustes_loss_weight=1.0, trans_weight=1, eval_registration=True, clip_weight_thresh=0.05, best_val_metric='succ_rate', inlier_model='ResUNetBN2C', inlier_feature_type='ones', inlier_conv1_kernel_size=3, inlier_knn=1, knn_search_method='gpu', inlier_use_direct_loss=True, feat_model='SimpleNetBN2C', feat_model_n_out=16, feat_conv1_kernel_size=3,
                    normalize_feature=True, use_xyz_feature=False, dist_type='L2', optimizer='SGD', max_epoch=100, lr=0.1, momentum=0.8, sgd_momentum=0.9, sgd_dampening=0.1, adam_beta1=0.9, adam_beta2=0.999, weight_decay=0.0001, iter_size=1, bn_momentum=0.05, exp_gamma=0.99, scheduler='ExpLR', num_train_iter=-1, icp_cache_path='icp', use_gpu=True, weights=None, weights_dir=None, resume=None, resume_dir=None, train_num_workers=2, val_num_workers=1, test_num_workers=2, fast_validation=False, nn_max_n=250, dataset='ThreeDMatchPairDataset03', voxel_size=0.025, threed_match_dir='.', kitti_dir=None, kitti_max_time_diff=3, kitti_date='2011_09_26', hit_ratio_thresh=0.1, success_rte_thresh=0.3, success_rre_thresh=15, test_random_crop=False, test_random_rotation=False, pcd0='redkitchen_000.ply', pcd1='redkitchen_010.ply')


class AttributeDict(object):
    def __init__(self, obj):
        self.obj = obj

    def __getstate__(self):
        return self.obj.items()

    def __setstate__(self, items):
        if not hasattr(self, 'obj'):
            self.obj = {}
        for key, val in items:
            self.obj[key] = val

    def __getattr__(self, name):
        if name in self.obj:
            return self.obj.get(name)
        else:
            return None

    def fields(self):
        return self.obj

    def keys(self):
        return self.obj.keys()


def get_config(update_dict={}):
    return AttributeDict(default_dict | update_dict)
