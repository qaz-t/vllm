# SPDX-License-Identifier: Apache-2.0
import random

import numpy as np
import torch

from vllm.platforms.interface import Platform


def test_seed_behavior():
    # Test with seed=None
    Platform.seed_everything(None)
    random_value_1 = random.randint(0, 100)
    np_random_value_1 = np.random.randint(0, 100)
    torch_random_value_1 = torch.randint(0, 100, (1, )).item()

    Platform.seed_everything(None)
    random_value_2 = random.randint(0, 100)
    np_random_value_2 = np.random.randint(0, 100)
    torch_random_value_2 = torch.randint(0, 100, (1, )).item()

    assert random_value_1 != random_value_2
    assert np_random_value_1 != np_random_value_2
    assert torch_random_value_1 != torch_random_value_2

    # Test with a specific seed
    Platform.seed_everything(42)
    random_value_3 = random.randint(0, 100)
    np_random_value_3 = np.random.randint(0, 100)
    torch_random_value_3 = torch.randint(0, 100, (1, )).item()

    Platform.seed_everything(42)
    random_value_4 = random.randint(0, 100)
    np_random_value_4 = np.random.randint(0, 100)
    torch_random_value_4 = torch.randint(0, 100, (1, )).item()

    assert random_value_3 == random_value_4
    assert np_random_value_3 == np_random_value_4
    assert torch_random_value_3 == torch_random_value_4
