from pathlib import Path


_root = Path(__file__).parent.resolve().joinpath('data')
_backend_folder = _root.joinpath('results')
_backend_folder.mkdir(exist_ok=True, parents=True)

_folders = {
    'data_folder_in': _root.joinpath('in'),
    'data_folder_out': _root.joinpath('in'),
    'processed_folder': _root.joinpath('processed')
}

for fn in _folders.values():
    fn.mkdir(exist_ok=True)



result_backend = 'file://{}'.format(str(_backend_folder))

broker_url = 'filesystem://'
broker_transport_options = {k: str(f) for k, f in _folders.items()}
task_serializer = 'json'
persist_results = True
result_serializer = 'json'
accept_content = ['json']
imports = ('tasks',)
