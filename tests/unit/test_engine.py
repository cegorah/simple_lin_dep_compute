from pandas.errors import EmptyDataError, ParserError
from app.engine.compute_engine import LDComputation


def test_add_task_correct(mocked_data):
    data = mocked_data()
    cmp = LDComputation()
    t_id = cmp.add_task(data)
    assert cmp.tasks_cnt > 0
    assert isinstance(t_id, str)


def test_add_task_incorrect(mocked_data):
    try:
        data = mocked_data(correct=False)
        cmp = LDComputation()
        cmp.add_task(data)
    except (EmptyDataError, ParserError):
        pass


def test_compute_correct(mocked_data):
    key = "1"
    data = mocked_data()
    cleaned_data = data.loc[:, (data.dtypes == "float64")]
    cmp = LDComputation()
    cmp.compute(cleaned_data, key)
    res_list = cmp.cache.get(key)
    assert isinstance(res_list, list)
    assert not res_list


def test_compute_correct_depend(mocked_data):
    key = "1"
    data = mocked_data(name="data1")
    cleaned_data = data.loc[:, (data.dtypes == "float64")]
    cmp = LDComputation()
    cmp.compute(cleaned_data, key)
    res_list = cmp.cache.get(key)
    assert isinstance(res_list, list)
    assert res_list == [2]
