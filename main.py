import os
import json
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--experiment_type", type=str, default="",
                            help="either 'training' or 'testing'")
parser.add_argument("--experiment_id", type=int, default="0",
                            help="id of json file")
parser.add_argument("--run", type=str, default="idle",
                            help="run to perform on experiment <id>, either 'idle' or 'config'")
parser.add_argument("--config", type=str, default="",
                            help="config instruction")

args = parser.parse_args()
print(args)

print("Experiment ID: " + str(args.experiment_id))

results_dir = './experiments/'
full_results_dir = results_dir + args.experiment_type + '/'

if args.run == 'config':
    if args.experiment_type == 'training':
        import trainID as run_exp
    elif args.experiment_type == 'testing':
        import testID as run_exp

    run_exp.config_experiments(full_results_dir)
    #     if args.config == 'generate':
#         run_exp.config_experiments(full_results_dir)

#     elif args.config == 'generate_datasets':
#         import runs.config_datasets as run
#         run.config_datasets(results_dir)

else:
    with open(full_results_dir + 'configs/' + str(args.experiment_id) + '.json') as config_file:
        config = json.load(config_file)

#     config['model_dir'] = full_results_dir + config['model_name']
#     config['results_dir'] = results_dir

#     with open(results_dir + 'configs_datasets/' + str(config["data_set"]) + '.json') as config_file:
#         config_dataset = json.load(config_file)
#     config["num_classes"] = config_dataset["num_classes"]  # This is going to be needed to define the architecture

    if args.experiment_type == 'training':
        import runs.train as run
        run.train(config)
    elif args.experiment_type == 'testing':
        import runs.test as run
        run.test(config)
