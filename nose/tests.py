from queue_status import Root()
import re

q = Root()

def test_run():
    task_id = q.run('tasks.add','1','2')
    reuuid = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9af]{4}-[0-9a-f]{12}')
    assert len(reuuid.findall(task_id)) == 1

