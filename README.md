# Best_fit_line
Using Python to find the best fit line of the experiment data

Experiment = A-level Physics past year (October/November 2004, 9702, Paper 5, Question 1)

![This is the output graph](data:image/png;base64,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aNjrn/LDu15hp83acfvJu9G2VfOsS5IkSUXIQLcaF154IU899dQqp6msrOTFF1+s03KffeMzTr9jNN02acvtJ/Wn3VqEuVtvvZWPPvpojeeXJEnFzfN7q3HJJZesdprKykratGnDnnvuWatlPv/mZ5xy6wi6btyeO0/uT/t1165l7tZbb6VHjx5sttlma7UcSZJUnMq6he7zzz/nmmuuWdl/wQUX8Ic//OFL05xwwgk88MADAHTp0oWLLrqI3r17s/POO/P666/z7rvvct1113H11VfTs2dPnn/+eT777DO++93v0q9fP/r168cLL7wAwK9+9SsGH3YEB+2/L3Mfv5qrv9mFE4/+Prvuuiu77rrryla+O++8k912242ePXvyX//1XyxbtgyANm3acOaZZ7LTTjsxcOBAPvvsMx544AFGjRrF0UcfTc+ePVmwYEFjfHSSJKkJKetA1759e26//XYAli9fzj333MMxxxyzynk6duzI6NGj+cEPfsBvf/tbunTpwumnn86ZZ57J2LFj2WeffTjjjDM488wzGTlyJH/729845ZRTAPjwi/lUjhjDnj++hteee5QLz/sZ++67L+PGjWP06NHstNNOTJo0iXvvvZcXXniBsWPHUlFRwV133QXAvHnz6Nu3LxMmTGDffffl4osv5vDDD6dv377cddddjB07ltatWzfshyZJkpqcsj7l2rx5czp06MCYMWP49NNP6dWrFx06dFjlPN/5zncA6NOnDw8++GC10zz11FNMnDhxZf/s2bOpfO19Hh77EZvtsjf3/HBfOrRpybBhw1YGyoqKCtq3b88dd9zBK6+8Qr9+/QBYsGABG220EQDrrLMO3//+9wE45phjVtYiSZLKW1kHOoBTTjmFW2+9lU8++YSTTjqJE088kTFjxrDZZpvx6KOPfmX6li1bArkAtnTp0mqXuXz5coYPH06rVq0AeOW9GRx308u0admM4762PZ3atqyxnpQSxx9/PFdcccVqa4+I2rxFSZJU4sr6lCvAt7/9bR5//HFGjhzJoEGDuOWWWxg7dmy1Ya4mbdu2Zc6cOSv7DzroIP70pz8BMOb9Lzji8nvYqF0rvttnc9q0/M8NEAMHDuSvf/0rAMuWLWPWrFkMHDiQBx54gGnTpgEwY8YM3nvvPSAXFFdcz3f33Xez9957V7t+SZJUXso+0LVo0YL9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)
