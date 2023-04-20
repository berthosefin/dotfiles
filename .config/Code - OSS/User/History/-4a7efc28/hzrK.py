from ship import navigate
from spaceship import fly


if argv[1] == 'navigate':
    navigate(argv[2])
elif argv[1] == 'fly':
    fly(argv[2])