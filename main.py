import mlflow

from run import args, main


def mlflow_run(args):
    with mlflow.start_run():
        mlflow.log_param('dataset', args.dataset)

        main(args)


if __name__ == '__main__':
    mlflow_run(args)
