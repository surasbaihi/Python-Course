{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The mean of the values = 28.22222222222222\n"
     ]
    }
   ],
   "source": [
    "import numpy\n",
    "a=[23,76,97,28,10,8,2,4,6]\n",
    "mean = numpy.mean(a)\n",
    "print(\"The mean of the values =\" , end = \" \")\n",
    "print(mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The mean of the values =  28.22222222222222\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=[23,76,97,28,10,8,2,4,6]\n",
    "mean = np.mean(a)\n",
    "print(\"The mean of the values = \" , end = \" \")\n",
    "print(mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The median of the values = 10.0\n"
     ]
    }
   ],
   "source": [
    "import numpy\n",
    "a=[23,76,97,28,10,8,2,4,6]\n",
    "median = numpy.median(a)\n",
    "print(\"The median of the values =\" , end = \" \")\n",
    "print(median)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The standard deviation of the values = 32.57394247546744\n"
     ]
    }
   ],
   "source": [
    "import numpy\n",
    "a=[23,76,97,28,10,8,2,4,6]\n",
    "standard_deviation = numpy.std(a)\n",
    "print(\"The standard deviation of the values =\" , end = \" \")\n",
    "print(standard_deviation) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The mean of the values = 28.22222222222222\n",
      "The median of the values = 10.0\n",
      "The standard deviation of the values = 32.57394247546744\n"
     ]
    }
   ],
   "source": [
    "from numpy import mean,median,std\n",
    "a=[23,76,97,28,10,8,2,4,6]\n",
    "print(\"The mean of the values =\" , mean(a))\n",
    "print(\"The median of the values =\" , median(a))\n",
    "print(\"The standard deviation of the values =\" , std(a))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
