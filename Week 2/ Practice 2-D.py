{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "states of jordan that starts with letter A :  Amman , Ajloun , Aqaba\n",
      "states of jordan that has 5 letters only: Amman ,  Irbid ,  Balqa ,  Zarqa ,  Karak , Ma'an , Aqaba\n"
     ]
    }
   ],
   "source": [
    "states_jordan_list = [\"Amman\",\"Irbid\",\"Ajloun\",\"Jerash\",\"Mafraq\",\"Balqa\",\"Zarqa\",\"Madaba\",\"Karak\",\"Tafila\",\"Ma'an\",\"Aqaba\"] \n",
    "\n",
    "print(\"states of jordan that starts with letter A :\" ,  end = \"  \")\n",
    "print(states_jordan_list[0] ,\",\" , end = \" \" )\n",
    "print(states_jordan_list[2] , \",\" , end = \" \")\n",
    "print(states_jordan_list[11])\n",
    "print(\"states of jordan that has 5 letters only:\" , end = \" \"  )\n",
    "print(states_jordan_list[0],\",\" ,end = \"  \")\n",
    "print(states_jordan_list[1],\",\", end = \"  \")\n",
    "print(states_jordan_list[5] ,\",\", end = \"  \")\n",
    "print(states_jordan_list[6] ,\",\" , end = \"  \")\n",
    "print(states_jordan_list[8],\",\" , end = \" \")\n",
    "print(states_jordan_list[10] ,\",\" , end = \" \")\n",
    "print(states_jordan_list[11])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "States of jordan that starts with letter 'A' = ['Amman', 'Ajloun', 'Aqaba']\n"
     ]
    }
   ],
   "source": [
    "states_jordan_list = [\"Amman\",\"Irbid\",\"Ajloun\",\"Jerash\",\"Mafraq\",\"Balqa\",\"Zarqa\",\"Madaba\",\"Karak\",\"Tafila\",\"Ma'an\",\"Aqaba\"]\n",
    "\n",
    "newlist=[ ]\n",
    "print(\"States of jordan that starts with letter 'A' =\" , end = \" \" )\n",
    "for word in states_jordan_list:\n",
    "    if word.startswith(\"A\"):\n",
    "        newlist.append(word)\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "States of jordan that starts with letter 'A' = ['Amman', 'Ajloun', 'Aqaba']\n"
     ]
    }
   ],
   "source": [
    "states_jordan_list = [\"Amman\",\"Irbid\",\"Ajloun\",\"Jerash\",\"Mafraq\",\"Balqa\",\"Zarqa\",\"Madaba\",\"Karak\",\"Tafila\",\"Ma'an\",\"Aqaba\"]\n",
    "newlist=[ ]\n",
    "print(\"States of jordan that starts with letter 'A' =\" , end = \" \" )\n",
    "for word in states_jordan_list:\n",
    "    if word[0]== \"A\":\n",
    "        newlist.append(word)\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "States of jordan that have 5 letters only =  ['Amman', 'Irbid', 'Balqa', 'Zarqa', 'Karak', \"Ma'an\", 'Aqaba']\n"
     ]
    }
   ],
   "source": [
    "states_jordan_list = [\"Amman\",\"Irbid\",\"Ajloun\",\"Jerash\",\"Mafraq\",\"Balqa\",\"Zarqa\",\"Madaba\",\"Karak\",\"Tafila\",\"Ma'an\",\"Aqaba\"] \n",
    "print(\"States of jordan that have 5 letters only = \" , end = \" \" )\n",
    "\n",
    "newlist=[ ]\n",
    "for word in states_jordan_list :\n",
    "    if len(word) == 5 :\n",
    "        newlist.append(word )\n",
    "print(newlist)"
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
