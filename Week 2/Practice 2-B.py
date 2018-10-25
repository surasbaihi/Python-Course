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
      "***Currency Converter***\n",
      "  ********Menu******** \n",
      "1:convert from JOD to TRY\n",
      "2:convert from TRY to JOD\n",
      "3:convert from TRY to USD\n",
      "4:convert from USD to TRY\n",
      "5:convert from JOD to USD\n",
      "6:convert from USD to JOD\n",
      "~~~~~~~~~~~~~~~~~~~~~~~~~\n",
      "Select from the menu : 1 or 2 or 3 or 4 or 5 or 6 : 1\n",
      "Enter amount of money in JOD you want to convert into TRY : 1\n",
      "Amount_TRY = 8.13\n"
     ]
    }
   ],
   "source": [
    "def currency_converter( ):\n",
    "    print(\"***Currency Converter***\")\n",
    "    print(\"  ********Menu******** \")\n",
    "    print(\"1:convert from JOD to TRY\")\n",
    "    print(\"2:convert from TRY to JOD\")\n",
    "    print(\"3:convert from TRY to USD\")\n",
    "    print(\"4:convert from USD to TRY\")\n",
    "    print(\"5:convert from JOD to USD\")\n",
    "    print(\"6:convert from USD to JOD\")\n",
    "    print(\"~~~~~~~~~~~~~~~~~~~~~~~~~\")\n",
    "    choice = input(\"Select from the menu : 1 or 2 or 3 or 4 or 5 or 6 : \")\n",
    "    exchangerate_JOD_TRY = 8.13\n",
    "    exchangerate_TRY_USD = 0.17\n",
    "    exchangerate_JOD_USD = 1.41\n",
    "    if choice == \"1\":\n",
    "        Amount_JOD = float(input(\"Enter amount of money in JOD you want to convert into TRY : \"))\n",
    "        Amount_TRY = Amount_JOD * exchangerate_JOD_TRY\n",
    "        print(\"Amount_TRY =\" , Amount_JOD * exchangerate_JOD_TRY )\n",
    "    elif choice == \"2\":\n",
    "        Amount_TRY = float(input(\"Enter amount of money in TRY you want to convert into JOD : \"))\n",
    "        Amount_JOD = Amount_TRY / exchangerate_JOD_TRY\n",
    "        print(\"Amount_JOD =\" , Amount_TRY / exchangerate_JOD_TRY )\n",
    "    elif choice == \"3\":\n",
    "        Amount_TRY = float(input(\"Enter amount of money in TRY you want to convert into USD : \"))\n",
    "        Amount_USD = Amount_TRY * exchangerate_TRY_USD\n",
    "        print(\"Amount_USD = \" ,Amount_TRY * exchangerate_TRY_USD )\n",
    "    elif choice == \"4\":\n",
    "        Amount_USD = float(input(\"Enter amount of money in USD you want to convert into TRY : \"))\n",
    "        Amount_TRY = Amount_USD / exchangerate_TRY_USD\n",
    "        print(\"Amount_TRY = \" ,Amount_USD / exchangerate_TRY_USD )\n",
    "    elif choice == \"5\":\n",
    "        Amount_JOD = float(input(\"Enter amount of money in JOD you want to convert into USD : \"))\n",
    "        Amount_USD = Amount_JOD * exchangerate_JOD_USD\n",
    "        print(\"Amount_USD =\" ,Amount_JOD * exchangerate_JOD_USD )\n",
    "    elif choice == \"6\":\n",
    "        Amount_USD = float(input(\"Enter amount of money in USD you want to convert into JOD : \"))\n",
    "        Amount_JOD = Amount_USD / exchangerate_JOD_USD\n",
    "        print(\"Amount_JOD = \", Amount_USD / exchangerate_JOD_USD )\n",
    "    else:\n",
    "        print(\"Exit Currency Converter\")\n",
    "currency_converter( )\n",
    "        "
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
