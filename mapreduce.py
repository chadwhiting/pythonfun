from datetime import date
from functools import reduce

obs = [
    (date.fromisoformat('2024-01-01'),'sharks',3),
    (date.fromisoformat('2024-01-02'),'sharks',2),
    (date.fromisoformat('2024-01-03'),'sharks',5),
    (date.fromisoformat('2024-02-01'),'sharks',1),
    (date.fromisoformat('2024-02-02'),'sharks',1),
    (date.fromisoformat('2024-02-03'),'sharks',2)
]

## transform
obs_dict = {}
for e in obs:
    month = e[0].month
    if month not in obs_dict:
       obs_dict[month] = []
    obs_dict[month].append(e[2])

## map, reduce
obs_dict =  \
    dict(
        map(
            lambda kv: (
                kv[0], 
                reduce(lambda v1, v2: v1 + v2, kv[1])
            ), 
            obs_dict.items()
        )
    )

print(obs_dict)
