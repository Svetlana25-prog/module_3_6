def calculate_structure_sum(data_structure):
    total_summa = 0

    def recurse(item):
      nonlocal total_summa
      if isinstance(item, (int, float)):
        total_summa += item
      elif isinstance(item, str):
        total_summa += len(item)
      elif isinstance(item, (list, tuple, set)):
        for sub_item in item:
          recurse(sub_item)
      elif isinstance(item, dict):
        for key, value in item.items():
          recurse(value)
          recurse(key)
    recurse(data_structure)
    return total_summa




data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)