echo [$(date)]:"Start"
conda init bash
# Installing jupyter
echo [$(date)]: " Mac M1 steps"
conda install -y jupyter --y
echo [$(date)]: "De-activating conda (If using Mac M1 and trying to install packages, this is must )"
echo [$(date)]: "Create env with python 3.10"
conda env create -f requirements_dev.yml
echo [$(date)]: "activating environment"
conda activate object_tracking_deepsort_V1
echo [$(date)]: "Register for jupyter notebook, This is for Mac M1"
python -m ipykernal install --user --name object_tracking_deepsort_V1 --display-name "Object tracking"
echo [$(date)]: "End"
