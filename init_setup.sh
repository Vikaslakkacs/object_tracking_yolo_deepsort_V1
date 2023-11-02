echo [$(date)]: 'START'
echo [$(date)]: "Creating environment with latest python version"
conda create --prefix object_tracking_deepsort_V1 python=3.10 -y
echo [$(date)]: "Activating environment"
source activate object_tracking_deepsort_V1
echp  [$(date)]: "Installing Dev requirements"
pip install -r requirements.txt
echo [$(date)]: "END"