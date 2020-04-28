import os
import shutil
from prodglob import prodglob, pathprod, prodmake


TEST_DIR = os.path.dirname(__file__)


PATH_ITEMS = TEST_DIR, 'base', ('a', 'b'), 'something', ('c', 'd')

ROOT_DIR = os.path.join(TEST_DIR, 'base')

EXPECTED_PATHS = (
    os.path.join(TEST_DIR, 'base/a/something/c'),
    os.path.join(TEST_DIR, 'base/a/something/d'),
    os.path.join(TEST_DIR, 'base/b/something/c'),
    os.path.join(TEST_DIR, 'base/b/something/d'),
)



def test_core():
    # check path product
    fs = pathprod(*PATH_ITEMS)
    assert tuple(fs) == EXPECTED_PATHS

    # check glob
    fs = prodglob(*PATH_ITEMS)
    assert tuple(fs) == ()

    # check files don't exist
    fs = pathprod(*PATH_ITEMS)
    assert sum(os.path.exists(f) for f in fs) == 0

    # check path make
    fs = prodmake(*PATH_ITEMS)
    assert sum(os.path.exists(f) for f in fs) == len(EXPECTED_PATHS)

    # check glob after making files
    fs = prodglob(*PATH_ITEMS)
    assert tuple(fs) == EXPECTED_PATHS

    # cleanup
    shutil.rmtree(ROOT_DIR)
