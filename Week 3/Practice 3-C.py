{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Week1_List =  ['.ipynb_checkpoints', 'Engineering.txt', 'Practice 1-A.py', 'Practice 1-B.py', 'Practice 1-E.pdf', 'Practice 1-F.pdf', 'Practice 1-G.pdf', 'Practice1-C.py']\n",
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
      "Enter file name you want to rename in week1 :Engineering.txt\n",
      "Enter the new file name :Read me.txt\n",
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
      "Week1_Newlist =  ['.ipynb_checkpoints', 'Engineering.txt', 'Practice 1-A.py', 'Practice 1-B.py', 'Practice 1-E.pdf', 'Practice 1-F.pdf', 'Practice 1-G.pdf', 'Practice1-C.py', '.ipynb_checkpoints', 'Practice 1-A.py', 'Practice 1-B.py', 'Practice 1-E.pdf', 'Practice 1-F.pdf', 'Practice 1-G.pdf', 'Practice1-C.py', 'Read me.txt']\n",
      "*********************************\n",
      "Week2_List =  [' Practice 2-D.py', '.ipynb_checkpoints', 'Practice 2-A.py', 'Practice 2-B.py', 'Practice 2-C.py', 'Practice 2-E.pdf', 'Read me.txt']\n",
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
      "Enter file name you want to rename in week2 : Read me.txt\n",
      "Enter the new file name : Engineering.txt\n",
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",
      "Week2_Newlist =  [' Practice 2-D.py', '.ipynb_checkpoints', 'Practice 2-A.py', 'Practice 2-B.py', 'Practice 2-C.py', 'Practice 2-E.pdf', 'Read me.txt', ' Practice 2-D.py', '.ipynb_checkpoints', 'Engineering.txt', 'Practice 2-A.py', 'Practice 2-B.py', 'Practice 2-C.py', 'Practice 2-E.pdf']\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "week1_list = [ ]\n",
    "\n",
    "for file in os.listdir(\"C:/Users/butterfly/Desktop/Python Course/Week1\" ):\n",
    "    week1_list.append(file)\n",
    "print(\"Week1_List = \" ,week1_list)\n",
    "\n",
    "print(\"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\")\n",
    "\n",
    "os.chdir(\"C:/Users/butterfly/Desktop/Python Course/Week1\")\n",
    "filename1 = str(input(\"Enter file name you want to rename in week1 : \"))\n",
    "new_filename1 = str(input(\"Enter the new file name :\"))\n",
    "os.rename(filename1,new_filename1)\n",
    "\n",
    "for file in os.listdir(\"C:/Users/butterfly/Desktop/Python Course/Week1\" ):\n",
    "    week1_list.append(file)\n",
    "    \n",
    "print(\"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\")\n",
    "\n",
    "print(\"Week1_Newlist = \" ,week1_list)\n",
    "\n",
    "print(\"*********************************\")\n",
    "\n",
    "week2_list = [ ]\n",
    "\n",
    "for file in os.listdir(\"C:/Users/butterfly/Desktop/Python Course/Week2\"):\n",
    "    week2_list.append(file)\n",
    "    \n",
    "print(\"Week2_List = \" , week2_list)\n",
    "\n",
    "print(\"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\")\n",
    "\n",
    "\n",
    "os.chdir(\"C:/Users/butterfly/Desktop/Python Course/Week2\")\n",
    "filename2 = str(input(\"Enter file name you want to rename in week2 : \"))\n",
    "new_filename2 = str(input(\"Enter the new file name : \"))\n",
    "os.rename(filename2,new_filename2)\n",
    "\n",
    "for file in os.listdir(\"C:/Users/butterfly/Desktop/Python Course/Week2\"):\n",
    "    week2_list.append(file)\n",
    "    \n",
    "print(\"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\")\n",
    "\n",
    "print(\"Week2_Newlist = \" , week2_list)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
