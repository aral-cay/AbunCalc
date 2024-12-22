import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *
import subprocess
import os
import matplotlib.pyplot as plt
from itertools import repeat
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import statistics
import mplcursors
import math
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTk, NavigationToolbar2Tk)
from tkinter import messagebox
from tkinter.font import Font
import sys

from contextlib import suppress # in construction -demo-


# Creating the ui screen
ui = Tk()
ui.title("AbunCalc -- v1.0")

# Getting the window info to create a suitable screen
height = 720
width = 1280

ui.geometry(f'{width}x{height}')

checkbox_control = 0


def passingThis():           # This function and the following two lines are to solve the on-hover problem for the lines
    print("")
    pass

sys.stderr = passingThis()
sys.stdout = passingThis()



# these functions are the radiobuttons
def radioselected_col1():
    global column_control
    column_control = 1


def radioselected_col2():
    global column_control
    column_control = 2


# these functions are for selecting the documents

def openfile_q1():
    global a_1
    global answer_label_1
    a_1 = askopenfilename(title='Select File')

    a_1_name = os.path.basename(a_1)

    answer_label_1.place_forget()

    answer_label_1 = tk.Label(ui, text=("Selected --->   " + a_1_name))
    answer_label_1.place(x=22, y=156, anchor='sw')


def openfile_q2():
    global a_2, a_3, a_2_name
    global answer_label_2
    a_2 = askopenfilename(title='Select File')

    a_2_name = os.path.basename(a_2)

    a_3_notready = os.path.basename(a_2)
    (a_3_stillnotready, ext) = os.path.splitext(a_3_notready)
    a_3 = (a_3_stillnotready + '.abundance')

    answer_label_2.place_forget()
    answer_label_2 = tk.Label(ui, text=("Selected --->   " + a_2_name))
    answer_label_2.place(x=22, y=218, anchor='sw')


def openfile_q4():
    global a_4
    global answer_label_4
    a_4 = askopenfilename(title='Select File')

    a_4_name = os.path.basename(a_4)

    answer_label_4.place_forget()

    answer_label_4 = tk.Label(ui, text=("Selected --->   " + a_4_name))
    answer_label_4.place(x=22, y=282, anchor='sw')


def open_info_screen():
    messagebox.showinfo("Information",
                        "--------------------------------------------------\n      AbunCalc version 1.0 ©, 2020 \n ------------------------------------------------- \n\n\n M. Taşkın Çay (mail@mail.com) \n                        & \n Aral Çay (mail@mail.com) \n\n                                   *** \n\n SPECTRUM suite © and Abundance © routine are property of \n Richard O. Gray (mail@mail.com) \n\n                                   *** \n\n If you use this program in your research, please give citation \n to the following papers: \n\n for AbunCalc: \n name of the paper, year, page, authors etc... \n\n for SPECTRUM and/or Abundance: \n name of the paper, year, page, authors etc...")


def checkbox_decision():
    global checkbox_control

    if boxstatus.get() == 1:
        checkbox_control = 1
    if boxstatus.get() == 0:
        checkbox_control = 0


def element_decision():
    global column_control
    global element_number2, element_number1

    if column_control == 1:
        token = open(a_3, 'r')
        linestoken = token.readlines()
        element_column1 = 1
        element_column_list1 = []

        for x in linestoken:
            element_column_list1.append(x.split()[element_column1])

        element_number1 = element_column_list1[0]

    if column_control == 2:
        token = open(a_3, 'r')
        linestoken = token.readlines()
        element_column2 = 1
        element_column_list2 = []

        for x in linestoken:
            element_column_list2.append(x.split()[element_column2])

        element_number2 = element_column_list2[0]


def draw_ionization_balance():
    global column_2_result_forgraph4, column_5_result_forgraph4, col_val_list_forgraph4, average_graph_1_forgraph4, col_val_list_forgraph4, standard_deviation_y_up_list_forgraph4
    global col_val_list_forgraph4, standard_deviation_y_down_list_forgraph4, col_2_min_forgraph4, col_2_max_forgraph4

    global column_2_result_forgraph1, column_5_result_forgraph1, col_val_list_forgraph1, average_graph_1_forgraph1, col_val_list_forgraph1, standard_deviation_y_up_list_forgraph1
    global col_val_list_forgraph1, standard_deviation_y_down_list_forgraph1, col_2_min_forgraph1, col_2_max_forgraph1
    global element_numberI
    global element_numberII
    global elementII_mean
    global elementI_mean

    global element_number
    global element_number2, element_number1

    

    fig_7 = plt.figure(7, figsize=(6, 3.5))

    try:
        mean_ofthe_means_label.place_forget()
        graph_7_scatter_mean_list_label.place_forget()
        difference_label.place_forget()
    except UnboundLocalError:
        pass

    plt.close(fig_7)

    fig_7 = plt.figure(7, figsize=(6, 3.5))

    plt.clf()

    graph_7 = fig_7.add_subplot(111)

    interface2 = Tk()
    interface2.title("Ionization Balance Graph")
    interface2.geometry("600x430")
    interface2.resizable(width=False, height=False)

        # for the black line

    average_graph_1_forcalc_forgraph1 = average_graph_1_forgraph1[0]
    average_graph_1_forcalc_forgraph4 = average_graph_1_forgraph4[0]

    mean_ofthe_means_notready = (average_graph_1_forcalc_forgraph1 + average_graph_1_forcalc_forgraph4) / 2
    mean_ofthe_means = []
    mean_ofthe_means.extend(repeat(mean_ofthe_means_notready, 2))

        # for the black dashed line
    scattersum1 = sum(column_5_result_forgraph1)
    scattersum2 = sum(column_5_result_forgraph4)
    scatterlen1 = len(column_5_result_forgraph1)
    scatterlen2 = len(column_5_result_forgraph4)

    finalscattersum = scattersum1 + scattersum2
    finalscatterlen = scatterlen1 + scatterlen2

    graph_7_scatter_mean = finalscattersum / finalscatterlen
    graph_7_scatter_mean_list = []
    graph_7_scatter_mean_list.extend(repeat(graph_7_scatter_mean, 2))

    if col_val_list_forgraph1[0] <= col_val_list_forgraph4[0]:
        col_val_list_x = col_val_list_forgraph1[0]

    elif col_val_list_forgraph1[0] >= col_val_list_forgraph4[0]:
        col_val_list_x = col_val_list_forgraph4[0]

    if col_val_list_forgraph1[1] >= col_val_list_forgraph4[1]:
        col_val_list_y = col_val_list_forgraph1[1]

    elif col_val_list_forgraph1[1] <= col_val_list_forgraph4[1]:
        col_val_list_y = col_val_list_forgraph4[1]

    col_val_list = [col_val_list_x, col_val_list_y]

    graph_7.scatter(column_2_result_forgraph1, column_5_result_forgraph1, color="blue", s=10)
    graph_7.plot(col_val_list, average_graph_1_forgraph1, color="blue")

    graph_7.scatter(column_2_result_forgraph4, column_5_result_forgraph4, color="red", s=10)
    graph_7.plot(col_val_list, average_graph_1_forgraph4, color="red")

    graph_7.plot(col_val_list, graph_7_scatter_mean_list, color="black", linestyle="--")
    graph_7.plot(col_val_list, mean_ofthe_means, color="black")

    graph_7.axis(ymin=mean_ofthe_means[0] - 0.7, ymax=mean_ofthe_means[0] + 0.7)

        

    plt.subplots_adjust(bottom=0.21)
    plt.xlabel("Excitation Potential (eV)", fontsize=9)
    plt.ylabel("log(A)", fontsize=9)

    canvas = FigureCanvasTkAgg(fig_7, master=interface2)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbarFrame = Frame(master=interface2)
    toolbarFrame.pack()
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

    mean_ofthe_means_value = str(round(mean_ofthe_means[0], 3))
    graph_7_scatter_mean_list_value = str(round(graph_7_scatter_mean_list[0], 3))

    difference_value = str(round(elementI_mean - elementII_mean, 3))
    if element_number1 != element_number2:

        mean_ofthe_means_label = tk.Label(interface2, text=("Mean: " + mean_ofthe_means_value), font=(8))
        mean_ofthe_means_label.place(x=230, y=420, anchor='sw')

        graph_7_scatter_mean_list_label = tk.Label(interface2,
                                                       text=("Weighted Mean: " + graph_7_scatter_mean_list_value), font=(8))
        graph_7_scatter_mean_list_label.place(x=390, y=420, anchor='sw')

        difference_label = tk.Label(interface2, text=(("Difference: " + difference_value)), font=(8))
        difference_label.place(x=10, y=420, anchor='sw')


        #fig_7.suptitle(("Ionization Balance for " + element_numberI.rstrip() + " and " + element_numberII), fontsize=10) ----instead \/

    

        headline_label  = tk.Label(interface2, text=(("Ionization balance for " + element_numberI.rstrip() + " and " + element_numberII)), bg ="white", font=(1))
        headline_label.place(x=185, y=0, anchor='nw')
        headline_label.config(font=('Helvatical bold',12))

    else:
        pass

    


# this function takes all the inputs and processes inputs to get the output
def mainprogram():
    global q_five_entry_input

    q_five_entry_input = q_five_entry.get()

    try:
        file = open(a_3, "r+")
        file.truncate(0)
        file.close()

    except FileNotFoundError:
        pass

    file = open("inputs.txt", "r+")
    file.truncate(0)
    file.close()

    with open("inputs.txt", "a") as f:
        f.write('{}\n{}\n{}\n{}\n{}\n'.format(a_1, a_2, a_3, a_4, q_five_entry_input))

    subprocess.call(r'abundance.exe -it <inputs.txt', shell=True)
    draw_graphs()
    create_panel()
    element_decision()
    if checkbox_control == 1:
        draw_ionization_balance()


# this function is for drawing the graphs

def draw_graphs():
    global average_y_forgraph1
    global average_y_round_forgraph1
    global standard_deviation_y_forgraph1, standard_error_str_forgraph1
    global column_control_forgraph1
    global xmin_forgraph1, xmax_forgraph1
    global column_2_result_forgraph1, column_5_result_forgraph1, col_val_list_forgraph1, average_graph_1_forgraph1, col_val_list_forgraph1, standard_deviation_y_up_list_forgraph1
    global col_val_list_forgraph1, standard_deviation_y_down_list_forgraph1, wavelength_result_forgraph1, col_2_min_forgraph1, col_2_max_forgraph1

    global average_y_forgraph4
    global average_y_round_forgraph4
    global standard_deviation_y_forgraph4, standard_error_str_forgraph4
    global column_control_forgraph4
    global xmin_forgraph4, xmax_forgraph4
    global column_2_result_forgraph4, column_5_result_forgraph4, col_val_list_forgraph4, average_graph_1_forgraph4, col_val_list_forgraph4, standard_deviation_y_up_list_forgraph4
    global col_val_list_forgraph4, standard_deviation_y_down_list_forgraph4, wavelength_result_forgraph4, col_2_min_forgraph4, col_2_max_forgraph4

    global graphname_label1
    global graphname_label2
    global confidence_level_str_forgraph4, solar_difference_result_forgraph4
    global confidence_level_str_forgraph1, solar_difference_result_forgraph1
    global element_numberI
    global element_numberII
    global elementII_mean
    global elementI_mean
    global element_number
    global b_forgraph4, b_forgraph1

    # Deciding the element

    token = open(a_3, 'r')
    linestoken = token.readlines()
    element_column = 1
    element_column_list = []

    for x in linestoken:
        element_column_list.append(x.split()[element_column])

    element_number = element_column_list[0]
    element_number_float = float(element_number)
    element_number_int = int(float(element_number))

    token = open(a_3, 'r')
    linestoken = token.readlines()
    column_5_forelement = 5
    column_5_list_forelement = []

    for x in linestoken:
        column_5_list_forelement.append(x.split()[column_5_forelement])

    column_5_result_forelement = [float(i) for i in column_5_list_forelement]

    a_forelement = sum(column_5_result_forelement)
    b_forelement = len(column_5_result_forelement)
    average_y_forelement = a_forelement / b_forelement
    token.close()

    if element_number_float > element_number_int:

        token = open("ElementsFile.txt", 'r')
        linestoken = token.readlines()
        element_number_int = element_number_int + 91
        element_numberII = linestoken[element_number_int]
        elementII_mean = average_y_forelement

        if column_control == 1:
            graphname_label1.place_forget()
            graphname_label1 = tk.Label(ui, text=(element_numberII), font=(15))
            graphname_label1.place(x=600, y=60, anchor='sw')

        if column_control == 2:
            graphname_label2.place_forget()
            graphname_label2 = tk.Label(ui, text=(element_numberII), font=(15))
            graphname_label2.place(x=1020, y=60, anchor='sw')

    if element_number_float == element_number_int:

        token = open("ElementsFile.txt", 'r')
        linestoken = token.readlines()
        element_number_int = element_number_int - 1
        element_numberI = linestoken[element_number_int]
        elementI_mean = average_y_forelement

        if column_control == 1:
            graphname_label1.place_forget()
            graphname_label1 = tk.Label(ui, text=(element_numberI), font=(15))
            graphname_label1.place(x=600, y=60, anchor='sw')

        if column_control == 2:
            graphname_label2.place_forget()
            graphname_label2 = tk.Label(ui, text=(element_numberI), font=(15))
            graphname_label2.place(x=1020, y=60, anchor='sw')

    if column_control == 1:

        token = open(a_3, 'r')
        linestoken = token.readlines()
        column_2_forgraph1 = 2
        column_2_list_forgraph1 = []

        for x in linestoken:
            column_2_list_forgraph1.append(x.split()[column_2_forgraph1])

        column_2_result_forgraph1 = [float(i) for i in column_2_list_forgraph1]

        col_2_min_forgraph1 = min(column_2_result_forgraph1)
        col_2_max_forgraph1 = max(column_2_result_forgraph1)

        col_2_min_ready_forgraph1 = col_2_min_forgraph1 - 0.6
        col_2_max_ready_forgraph1 = col_2_max_forgraph1 + 0.6

        col_val_list_forgraph1 = [col_2_min_ready_forgraph1, col_2_max_ready_forgraph1]

        token.close()
        ###########################################################################
        token = open(a_3, 'r')
        linestoken = token.readlines()
        column_5_forgraph1 = 5
        column_5_list_forgraph1 = []

        for x in linestoken:
            column_5_list_forgraph1.append(x.split()[column_5_forgraph1])

        column_5_result_forgraph1 = [float(i) for i in column_5_list_forgraph1]

        a_forgraph1 = sum(column_5_result_forgraph1)
        b_forgraph1 = len(column_5_result_forgraph1)
        average_y_forgraph1 = a_forgraph1 / b_forgraph1

        average_graph_1_forgraph1 = []
        average_graph_1_forgraph1.extend(repeat(average_y_forgraph1, 2))

        token.close()

        # rounding the mean

        average_y_round_forgraph1 = round(average_y_forgraph1, 2)
        average_y_round_forgraph1 = str(average_y_round_forgraph1)

        # calculating standard deviation

        standard_deviation_y_float_forgraph1 = statistics.stdev(column_5_result_forgraph1)
        standard_deviation_y_float_forgraph1 = round(standard_deviation_y_float_forgraph1, 2)
        standard_deviation_y_forgraph1 = str(standard_deviation_y_float_forgraph1)

        # calculation of the standard error
        standard_error_forgraph1 = standard_deviation_y_float_forgraph1 / math.sqrt(b_forgraph1)
        standard_error_forgraph1 = round(standard_error_forgraph1, 3)
        standard_error_str_forgraph1 = str(standard_error_forgraph1)

        # creating the positive standard deviation line
        standard_deviation_up_forgraph1 = average_y_forgraph1 + standard_deviation_y_float_forgraph1
        standard_deviation_up_forgraph1 = str(standard_deviation_up_forgraph1)
        standard_deviation_y_up_list_forgraph1 = []
        standard_deviation_y_up_list_forgraph1.extend(repeat(standard_deviation_up_forgraph1, 2))
        standard_deviation_y_up_list_forgraph1 = [float(i) for i in standard_deviation_y_up_list_forgraph1]

        # creating the negative standard deviation line
        standard_deviation_down_forgraph1 = average_y_forgraph1 - standard_deviation_y_float_forgraph1
        standard_deviation_down_forgraph1 = str(standard_deviation_down_forgraph1)
        standard_deviation_y_down_list_forgraph1 = []
        standard_deviation_y_down_list_forgraph1.extend(repeat(standard_deviation_down_forgraph1, 2))
        standard_deviation_y_down_list_forgraph1 = [float(i) for i in standard_deviation_y_down_list_forgraph1]

        # calculation of confidence level

        confidence_level_forgraph1 = (standard_deviation_y_float_forgraph1 * 1.96) / math.sqrt(b_forgraph1 + 1)
        confidence_level_forgraph1 = round(confidence_level_forgraph1, 3)
        confidence_level_str_forgraph1 = str(confidence_level_forgraph1)

        # Creating the positive 95% confidence line

        confidence_level_up_forgraph1 = average_y_forgraph1 + confidence_level_forgraph1
        confidence_level_up_forgraph1 = str(confidence_level_up_forgraph1)
        confidence_level_up_list_forgraph1 = []
        confidence_level_up_list_forgraph1.extend(repeat(confidence_level_up_forgraph1, 2))
        confidence_level_up_list_forgraph1 = [float(i) for i in [float(i) for i in confidence_level_up_list_forgraph1]]

        # Creating the negative 95% confidence line

        confidence_level_down_forgraph1 = average_y_forgraph1 - confidence_level_forgraph1
        confidence_level_down_forgraph1 = str(confidence_level_down_forgraph1)
        confidence_level_down_list_forgraph1 = []
        confidence_level_down_list_forgraph1.extend(repeat(confidence_level_down_forgraph1, 2))
        confidence_level_down_list_forgraph1 = [float(i) for i in
                                                [float(i) for i in confidence_level_down_list_forgraph1]]

        # calculation of solar difference

        token = open(a_3, 'r')
        linestoken = token.readlines()
        solar_difference_column = 6
        solar_difference_list = []
        for x in linestoken:
            solar_difference_list.append(x.split()[solar_difference_column])

        solar_difference_list = [float(i) for i in solar_difference_list]
        solar_difference_len = len(solar_difference_list)
        solar_difference_sum = sum(solar_difference_list)
        solar_difference_result_forgraph1 = solar_difference_sum / solar_difference_len
        solar_difference_result_forgraph1 = round(solar_difference_result_forgraph1, 3)

        # Linear fit

        model = np.polyfit(column_2_result_forgraph1, column_5_result_forgraph1, 1)
        poly = np.poly1d(model)
        new_x = np.linspace(col_val_list_forgraph1[0], col_val_list_forgraph1[-1])
        new_y = poly(new_x)

        ###########################################################################

        token = open(a_3, 'r')
        linestoken = token.readlines()
        wavelength_col_forgraph1 = 0
        wavelength_list_forgraph1 = []
        for x in linestoken:
            wavelength_list_forgraph1.append(x.split()[wavelength_col_forgraph1])

        wavelength_result_forgraph1 = [float(i) for i in wavelength_list_forgraph1]

        fig_1 = plt.figure(1, figsize=(4, 2.1))

        plt.clf()

        graph_1 = fig_1.add_subplot(111)
        plt.subplots_adjust(left=0.15)
        graph_1.tick_params(labelsize=8)

        graph_1.scatter(column_2_result_forgraph1, column_5_result_forgraph1, color="blue", s=5)

        graph_1.plot(new_x, new_y, color="limegreen")

        graph_1.plot(col_val_list_forgraph1, average_graph_1_forgraph1, color='black', dashes=(2, 2))

        graph_1.plot(col_val_list_forgraph1, standard_deviation_y_up_list_forgraph1, color='blue')
        graph_1.plot(col_val_list_forgraph1, standard_deviation_y_down_list_forgraph1, color='blue')

        graph_1.plot(col_val_list_forgraph1, confidence_level_up_list_forgraph1, color='blue', linewidth=0.5,
                     dashes=(2, 2))
        graph_1.plot(col_val_list_forgraph1, confidence_level_down_list_forgraph1, color='blue', linewidth=0.5,
                     dashes=(2, 2))

        graph_1.axis(xmin=col_2_min_forgraph1 - 0.5, xmax=col_2_max_forgraph1 + 0.5)


        ## Setting y Limits to the graph
        token = open(a_3, 'r')
        linestoken = token.readlines()
        column_5_forgraph1 = 5
        column_5_list_forgraph1 = []

        for x in linestoken:
            column_5_list_forgraph1.append(x.split()[column_5_forgraph1])

        column_5_result_forgraph1 = [float(i) for i in column_5_list_forgraph1] 
        minimumValofGraph1 = min(column_5_result_forgraph1)
        maximumValofGraph1 = max(column_5_result_forgraph1)
        token.close()
        
        graph_1.axis(ymin=minimumValofGraph1 - 0.15, ymax=maximumValofGraph1 + 0.15)
        ##

        # Slope for graph 1

        slope_forgraph1 = round(model[0], 3)
        slope_forgraph1 = str(slope_forgraph1)
        fig_1.text(0.7, 0.9, ("slope: " + slope_forgraph1))

        plt.subplots_adjust(bottom=0.21)
        plt.xlabel("Excitation Potential (eV)", fontsize=9)
        plt.ylabel("log(A)", fontsize=9)

        canvas = FigureCanvasTkAgg(fig_1, master=ui)
        canvas.draw()
        canvas.get_tk_widget().place(x=425, y=255, anchor="sw")


        
        mplcursors.cursor(graph_1, hover=True).connect(
                    "add", lambda sel: sel.annotation.set_text(wavelength_result_forgraph1[sel.target.index]))


    if column_control == 2:

        #############################################

        token = open(a_3, 'r')
        linestoken = token.readlines()
        column_2_forgraph4 = 2
        column_2_list_forgraph4 = []

        for x in linestoken:
            column_2_list_forgraph4.append(x.split()[column_2_forgraph4])

        column_2_result_forgraph4 = [float(i) for i in column_2_list_forgraph4]

        col_2_min_forgraph4 = min(column_2_result_forgraph4)
        col_2_max_forgraph4 = max(column_2_result_forgraph4)

        col_2_min_ready_forgraph4 = col_2_min_forgraph4 - 0.6
        col_2_max_ready_forgraph4 = col_2_max_forgraph4 + 0.6

        col_val_list_forgraph4 = [col_2_min_ready_forgraph4, col_2_max_ready_forgraph4]

        token.close()
        ###########################################################################
        token = open(a_3, 'r')
        linestoken = token.readlines()
        column_5_forgraph4 = 5
        column_5_list_forgraph4 = []

        for x in linestoken:
            column_5_list_forgraph4.append(x.split()[column_5_forgraph4])

        column_5_result_forgraph4 = [float(i) for i in column_5_list_forgraph4]

        a_forgraph4 = sum(column_5_result_forgraph4)
        b_forgraph4 = len(column_5_result_forgraph4)
        average_y_forgraph4 = a_forgraph4 / b_forgraph4

        average_graph_1_forgraph4 = []
        average_graph_1_forgraph4.extend(repeat(average_y_forgraph4, 2))

        token.close()

        # rounding the mean

        average_y_round_forgraph4 = round(average_y_forgraph4, 2)
        average_y_round_forgraph4 = str(average_y_round_forgraph4)

        # calculating standard deviation

        standard_deviation_y_float_forgraph4 = statistics.stdev(column_5_result_forgraph4)
        standard_deviation_y_float_forgraph4 = round(standard_deviation_y_float_forgraph4, 2)
        standard_deviation_y_forgraph4 = str(standard_deviation_y_float_forgraph4)

        # calculation of the standard error
        standard_error_forgraph4 = standard_deviation_y_float_forgraph4 / math.sqrt(b_forgraph4)
        standard_error_forgraph4 = round(standard_error_forgraph4, 3)
        standard_error_str_forgraph4 = str(standard_error_forgraph4)

        # creating the positive standard deviation line
        standard_deviation_up_forgraph4 = average_y_forgraph4 + standard_deviation_y_float_forgraph4
        standard_deviation_up_forgraph4 = str(standard_deviation_up_forgraph4)
        standard_deviation_y_up_list_forgraph4 = []
        standard_deviation_y_up_list_forgraph4.extend(repeat(standard_deviation_up_forgraph4, 2))
        standard_deviation_y_up_list_forgraph4 = [float(i) for i in standard_deviation_y_up_list_forgraph4]

        # creating the negative standard deviation line
        standard_deviation_down_forgraph4 = average_y_forgraph4 - standard_deviation_y_float_forgraph4
        standard_deviation_down_forgraph4 = str(standard_deviation_down_forgraph4)
        standard_deviation_y_down_list_forgraph4 = []
        standard_deviation_y_down_list_forgraph4.extend(repeat(standard_deviation_down_forgraph4, 2))
        standard_deviation_y_down_list_forgraph4 = [float(i) for i in standard_deviation_y_down_list_forgraph4]

        # calculation of confidence level

        confidence_level_forgraph4 = (standard_deviation_y_float_forgraph4 * 1.96) / math.sqrt(b_forgraph4 + 1)
        confidence_level_forgraph4 = round(confidence_level_forgraph4, 3)
        confidence_level_str_forgraph4 = str(confidence_level_forgraph4)

        # Creating the positive 95% confidence line

        confidence_level_up_forgraph4 = average_y_forgraph4 + confidence_level_forgraph4
        confidence_level_up_forgraph4 = str(confidence_level_up_forgraph4)
        confidence_level_up_list_forgraph4 = []
        confidence_level_up_list_forgraph4.extend(repeat(confidence_level_up_forgraph4, 2))
        confidence_level_up_list_forgraph4 = [float(i) for i in [float(i) for i in confidence_level_up_list_forgraph4]]

        # Creating the negative 95% confidence line

        confidence_level_down_forgraph4 = average_y_forgraph4 - confidence_level_forgraph4
        confidence_level_down_forgraph4 = str(confidence_level_down_forgraph4)
        confidence_level_down_list_forgraph4 = []
        confidence_level_down_list_forgraph4.extend(repeat(confidence_level_down_forgraph4, 2))
        confidence_level_down_list_forgraph4 = [float(i) for i in
                                                [float(i) for i in confidence_level_down_list_forgraph4]]

        # calculation of solar difference
        token = open(a_3, 'r')
        linestoken = token.readlines()
        solar_difference_column = 6
        solar_difference_list = []
        for x in linestoken:
            solar_difference_list.append(x.split()[solar_difference_column])

        solar_difference_list = [float(i) for i in solar_difference_list]

        solar_difference_list = [float(i) for i in solar_difference_list]
        solar_difference_len = len(solar_difference_list)
        solar_difference_sum = sum(solar_difference_list)
        solar_difference_result_forgraph4 = solar_difference_sum / solar_difference_len
        solar_difference_result_forgraph4 = round(solar_difference_result_forgraph4, 3)

        # Linear fit

        model = np.polyfit(column_2_result_forgraph4, column_5_result_forgraph4, 1)
        poly = np.poly1d(model)
        new_x = np.linspace(col_val_list_forgraph4[0], col_val_list_forgraph4[-1])
        new_y = poly(new_x)

        ###########################################################################

        token = open(a_3, 'r')
        linestoken = token.readlines()
        wavelength_col_forgraph4 = 0
        wavelength_list_forgraph4 = []
        for x in linestoken:
            wavelength_list_forgraph4.append(x.split()[wavelength_col_forgraph4])

        wavelength_result_forgraph4 = [float(i) for i in wavelength_list_forgraph4]

        fig_4 = plt.figure(4, figsize=(4, 2.4))

        plt.clf()

        graph_4 = fig_4.add_subplot(111)

        plt.subplots_adjust(left=0.15)
        graph_4.tick_params(labelsize=8)

        graph_4.scatter(column_2_result_forgraph4, column_5_result_forgraph4, color="red", s=5)

        graph_4.plot(col_val_list_forgraph4, average_graph_1_forgraph4, color="black", dashes=(2, 2))

        graph_4.plot(new_x, new_y, color="limegreen")

        graph_4.plot(col_val_list_forgraph4, standard_deviation_y_up_list_forgraph4, color="red")
        graph_4.plot(col_val_list_forgraph4, standard_deviation_y_down_list_forgraph4, color="red")

        graph_4.plot(col_val_list_forgraph4, confidence_level_up_list_forgraph4, color='red', linewidth=0.5,
                     dashes=(2, 2))
        graph_4.plot(col_val_list_forgraph4, confidence_level_down_list_forgraph4, color='red', linewidth=0.5,
                     dashes=(2, 2))

        graph_4.axis(xmin=col_2_min_forgraph4 - 0.5, xmax=col_2_max_forgraph4 + 0.5)


        ## Setting y Limits to the graph
        token = open(a_3, 'r')
        linestoken = token.readlines()
        column_5_forgraph4 = 5
        column_5_list_forgraph4 = []

        for x in linestoken:
            column_5_list_forgraph4.append(x.split()[column_5_forgraph4])

        column_5_result_forgraph4 = [float(i) for i in column_5_list_forgraph4] 
        minimumValofGraph4 = min(column_5_result_forgraph4)
        maximumValofGraph4 = max(column_5_result_forgraph4)
        token.close()
        
        graph_4.axis(ymin=minimumValofGraph4 - 0.15, ymax=maximumValofGraph4 + 0.15)
        ##



        # Slope for graph 4

        slope_forgraph4 = round(model[0], 3)
        slope_forgraph4 = str(slope_forgraph4)
        fig_4.text(0.7, 0.9, ("slope: " + slope_forgraph4))

        plt.subplots_adjust(bottom=0.21)
        plt.xlabel("Excitation Potential (eV)", fontsize=9)
        plt.ylabel("log(A)", fontsize=9)

        canvas = FigureCanvasTkAgg(fig_4, master=ui)
        canvas.draw()
        canvas.get_tk_widget().place(x=850, y=255, anchor="sw")

        mplcursors.cursor(graph_4, hover=True).connect(
            "add", lambda sel: sel.annotation.set_text(wavelength_result_forgraph4[sel.target.index]))

        token.close()

    if column_control == 1:

        token = open(a_2, 'r')
        linestoken = token.readlines()
        col_num_7 = 7
        col_num_0 = 0
        column_8_list_forgraph2 = []

        wavelength_list_forgraph2 = []

        for x in linestoken:
            wavelength_forgraph2 = x.split()[col_num_0]
            wavelength_forgraph2 = float(wavelength_forgraph2)
            wavelength_list_forgraph2.append(wavelength_forgraph2)

            a = x.split()[col_num_7]
            a = float(a)

            a = math.log(((a / 1000) / wavelength_forgraph2), 10)
            column_8_list_forgraph2.append(a)

        fig_2 = plt.figure(2, figsize=(4, 2.1))
        plt.clf()
        graph_2 = fig_2.add_subplot(111)

        plt.subplots_adjust(left=0.15)
        graph_2.tick_params(labelsize=8)

        column_8_list_min_forgraph_2 = min(column_8_list_forgraph2)
        column_8_list_max_forgraph_2 = max(column_8_list_forgraph2)
        column_8_list_min_forgraph_2 = column_8_list_min_forgraph_2 - 0.1
        column_8_list_max_forgraph_2 = column_8_list_max_forgraph_2 + 0.1
        col_val_list_forgraph2 = [column_8_list_min_forgraph_2, column_8_list_max_forgraph_2]

        # Linear fit

        model = np.polyfit(column_8_list_forgraph2, column_5_result_forgraph1, 1)
        poly = np.poly1d(model)
        new_x = np.linspace(col_val_list_forgraph2[0], col_val_list_forgraph2[-1])
        new_y = poly(new_x)

        graph_2.plot(new_x, new_y, color="limegreen")

        graph_2.scatter(column_8_list_forgraph2, column_5_result_forgraph1, color="blue", s=5)
        graph_2.plot(col_val_list_forgraph2, average_graph_1_forgraph1, color="black", dashes=(2, 2))

        graph_2.plot(col_val_list_forgraph2, standard_deviation_y_up_list_forgraph1, color="blue")
        graph_2.plot(col_val_list_forgraph2, standard_deviation_y_down_list_forgraph1, color="blue")

        graph_2.plot(col_val_list_forgraph2, confidence_level_up_list_forgraph1, color='blue', linewidth=0.5,
                     dashes=(2, 2))
        graph_2.plot(col_val_list_forgraph2, confidence_level_down_list_forgraph1, color='blue', linewidth=0.5,
                     dashes=(2, 2))

        graph_2.axis(xmin=column_8_list_min_forgraph_2, xmax=column_8_list_max_forgraph_2)

        graph_2.axis(ymin=minimumValofGraph1 - 0.15, ymax=maximumValofGraph1 + 0.15)
        # Slope for graph 2

        slope_forgraph2 = round(model[0], 3)
        slope_forgraph2 = str(slope_forgraph2)
        fig_2.text(0.7, 0.9, ("slope: " + slope_forgraph2))

        plt.subplots_adjust(bottom=0.21)
        plt.xlabel("Reduced E.W.", fontsize=9)
        plt.ylabel("log(A)", fontsize=9)
        canvas = FigureCanvasTkAgg(fig_2, master=ui)
        canvas.draw()
        canvas.get_tk_widget().place(x=425, y=480, anchor="sw")

        mplcursors.cursor(graph_2, hover=True).connect(
            "add", lambda sel: sel.annotation.set_text(wavelength_list_forgraph2[sel.target.index]))

    if column_control == 2:

        token = open(a_2, 'r')
        linestoken = token.readlines()
        col_num_7 = 7
        col_num_0 = 0
        column_8_list_forgraph5 = []

        wavelength_list_forgraph5 = []

        for x in linestoken:
            wavelength_forgraph5 = x.split()[col_num_0]
            wavelength_forgraph5 = float(wavelength_forgraph5)

            wavelength_list_forgraph5.append(wavelength_forgraph5)

            a = x.split()[col_num_7]
            a = float(a)

            a = math.log(((a / 1000) / wavelength_forgraph5), 10)
            column_8_list_forgraph5.append(a)

        fig_5 = plt.figure(5, figsize=(4, 2.1))
        plt.clf()
        graph_5 = fig_5.add_subplot(111)

        plt.subplots_adjust(left=0.15)
        graph_5.tick_params(labelsize=8)

        column_8_list_min_forgraph_5 = min(column_8_list_forgraph5)
        column_8_list_max_forgraph_5 = max(column_8_list_forgraph5)
        column_8_list_min_forgraph_5 = column_8_list_min_forgraph_5 - 0.1
        column_8_list_max_forgraph_5 = column_8_list_max_forgraph_5 + 0.1
        col_val_list_forgraph5 = [column_8_list_min_forgraph_5, column_8_list_max_forgraph_5]

        # Linear fit

        model = np.polyfit(column_8_list_forgraph5, column_5_result_forgraph4, 1)
        poly = np.poly1d(model)
        new_x = np.linspace(col_val_list_forgraph5[0], col_val_list_forgraph5[-1])
        new_y = poly(new_x)

        graph_5.plot(new_x, new_y, color="limegreen")

        graph_5.scatter(column_8_list_forgraph5, column_5_result_forgraph4, color="red", s=5)
        graph_5.plot(col_val_list_forgraph5, average_graph_1_forgraph4, color="black", dashes=(2, 2))
        graph_5.plot(col_val_list_forgraph5, standard_deviation_y_up_list_forgraph4, color="red")
        graph_5.plot(col_val_list_forgraph5, standard_deviation_y_down_list_forgraph4, color="red")
        graph_5.plot(col_val_list_forgraph5, confidence_level_up_list_forgraph4, color='red', linewidth=0.5,
                     dashes=(2, 2))
        graph_5.plot(col_val_list_forgraph5, confidence_level_down_list_forgraph4, color='red', linewidth=0.5,
                     dashes=(2, 2))
        graph_5.axis(xmin=column_8_list_min_forgraph_5, xmax=column_8_list_max_forgraph_5)
        graph_5.axis(ymin=minimumValofGraph4 - 0.15, ymax=maximumValofGraph4 + 0.15)
        
        # Slope for graph 5

        slope_forgraph5 = round(model[0], 3)
        slope_forgraph5 = str(slope_forgraph5)
        fig_5.text(0.7, 0.9, ("slope: " + slope_forgraph5))

        plt.subplots_adjust(bottom=0.21)
        plt.xlabel("Reduced E.W.", fontsize=9)
        plt.ylabel("log(A)", fontsize=9)
        canvas = FigureCanvasTkAgg(fig_5, master=ui)
        canvas.draw()
        canvas.get_tk_widget().place(x=850, y=480, anchor="sw")
        mplcursors.cursor(graph_5, hover=True).connect(
            "add", lambda sel: sel.annotation.set_text(wavelength_list_forgraph5[sel.target.index]))

    if column_control == 1:
        fig_3 = plt.figure(3, figsize=(4, 2.1))

        plt.clf()

        graph_3 = fig_3.add_subplot(111)

        plt.subplots_adjust(left=0.15)
        graph_3.tick_params(labelsize=8)

        wave_length_min_forgraph3 = min(wavelength_result_forgraph1)
        wave_length_max_forgraph3 = max(wavelength_result_forgraph1)
        wave_length_min_ready_forgraph3 = wave_length_min_forgraph3 - 250
        wave_length_max_ready_forgraph3 = wave_length_max_forgraph3 + 250
        col_val_list_forgraph3 = [wave_length_min_ready_forgraph3, wave_length_max_ready_forgraph3]

        # Linear fit

        model = np.polyfit(wavelength_result_forgraph1, column_5_result_forgraph1, 1)
        poly = np.poly1d(model)
        new_x = np.linspace(col_val_list_forgraph3[0], col_val_list_forgraph3[-1])
        new_y = poly(new_x)

        graph_3.plot(new_x, new_y, color="limegreen")

        graph_3.scatter(wavelength_result_forgraph1, column_5_result_forgraph1, color="blue", s=5)
        graph_3.plot(col_val_list_forgraph3, average_graph_1_forgraph1, color="black", dashes=(2, 2))
        graph_3.plot(col_val_list_forgraph3, standard_deviation_y_up_list_forgraph1, color="blue")
        graph_3.plot(col_val_list_forgraph3, standard_deviation_y_down_list_forgraph1, color="blue")
        graph_3.plot(col_val_list_forgraph3, confidence_level_up_list_forgraph1, color='blue', linewidth=0.5,
                     dashes=(2, 2))
        graph_3.plot(col_val_list_forgraph3, confidence_level_down_list_forgraph1, color='blue', linewidth=0.5,
                     dashes=(2, 2))
        graph_3.axis(xmin=wave_length_min_ready_forgraph3 - 0.2, xmax=wave_length_max_ready_forgraph3 + 0.2)
        graph_3.axis(ymin=minimumValofGraph1 - 0.15, ymax=maximumValofGraph1 + 0.15)
        # Slope for graph 3

        slope_forgraph3 = round(model[0], 3)
        slope_forgraph3 = str(slope_forgraph3)
        fig_3.text(0.7, 0.9, ("slope: " + slope_forgraph3))

        plt.subplots_adjust(bottom=0.21)
        plt.xlabel("Wavelength (Å)", fontsize=9)
        plt.ylabel("log(A)", fontsize=9)
        canvas = FigureCanvasTkAgg(fig_3, master=ui)
        canvas.draw()
        canvas.get_tk_widget().place(x=425, y=705, anchor="sw")

        mplcursors.cursor(graph_3, hover=True).connect(
            "add", lambda sel: sel.annotation.set_text(wavelength_result_forgraph1[sel.target.index]))

    if column_control == 2:
        fig_6 = plt.figure(6, figsize=(4, 2.1))

        plt.clf()

        graph_6 = fig_6.add_subplot(111)

        plt.subplots_adjust(left=0.15)
        graph_6.tick_params(labelsize=8)

        wave_length_min_forgraph6 = min(wavelength_result_forgraph4)
        wave_length_max_forgraph6 = max(wavelength_result_forgraph4)
        wave_length_min_ready_forgraph6 = wave_length_min_forgraph6 - 250
        wave_length_max_ready_forgraph6 = wave_length_max_forgraph6 + 250
        col_val_list_forgraph6 = [wave_length_min_ready_forgraph6, wave_length_max_ready_forgraph6]

        # Linear fit

        model = np.polyfit(wavelength_result_forgraph4, column_5_result_forgraph4, 1)
        poly = np.poly1d(model)
        new_x = np.linspace(col_val_list_forgraph6[0], col_val_list_forgraph6[-1])
        new_y = poly(new_x)

        graph_6.plot(new_x, new_y, color="limegreen")

        graph_6.scatter(wavelength_result_forgraph4, column_5_result_forgraph4, color="red", s=5)
        graph_6.plot(col_val_list_forgraph6, average_graph_1_forgraph4, color="black", dashes=(2, 2))
        graph_6.plot(col_val_list_forgraph6, standard_deviation_y_up_list_forgraph4, color="red")
        graph_6.plot(col_val_list_forgraph6, standard_deviation_y_down_list_forgraph4, color="red")
        graph_6.plot(col_val_list_forgraph6, confidence_level_up_list_forgraph4, color='red', linewidth=0.5,
                     dashes=(2, 2))
        graph_6.plot(col_val_list_forgraph6, confidence_level_down_list_forgraph4, color='red', linewidth=0.5,
                     dashes=(2, 2))
        graph_6.axis(xmin=wave_length_min_ready_forgraph6 - 0.2, xmax=wave_length_max_ready_forgraph6 + 0.2)
        graph_6.axis(ymin=minimumValofGraph4 - 0.15, ymax=maximumValofGraph4 + 0.15)
        # Slope for graph 6

        slope_forgraph6 = round(model[0], 3)
        slope_forgraph6 = str(slope_forgraph6)
        fig_6.text(0.7, 0.9, ("slope: " + slope_forgraph6))

        plt.subplots_adjust(bottom=0.21)
        plt.xlabel("Wavelength (Å)", fontsize=9)
        plt.ylabel("log(A)", fontsize=9)
        canvas = FigureCanvasTkAgg(fig_6, master=ui)
        canvas.draw()
        canvas.get_tk_widget().place(x=850, y=705, anchor="sw")

        mplcursors.cursor(graph_6, hover=True).connect(
            "add", lambda sel: sel.annotation.set_text(wavelength_result_forgraph4[sel.target.index]))


# Creating the panel

def create_panel():
    global model_info_label1
    global model_info_label2
    global loga_info_label1
    global loga_info_label2
    global standardd_info_label1
    global standardd_info_label2
    global standarde_info_label1
    global standarde_info_label2
    global microturbulance_info_label1
    global microturbulance_info_label2
    global conflvl_info_label1
    global conflvl_info_label2
    global elementh_info_label1
    global elementh_info_label2
    global confidence_level_str_forgraph4
    global confidence_level_str_forgraph1
    global b_forgraph4, b_forgraph1
    global lineamount_info_label1, lineamount_info_label2

    model_name_notready = os.path.basename(a_1)
    (model_name, ext) = os.path.splitext(model_name_notready)

    if column_control == 1:

        model_info_label1.place_forget()
        loga_info_label1.place_forget()
        standardd_info_label1.place_forget()
        standarde_info_label1.place_forget()
        microturbulance_info_label1.place_forget()
        conflvl_info_label1.place_forget()
        elementh_info_label1.place_forget()
        lineamount_info_label1.place_forget()

        model_lenght_graph1 = len(model_name)
        if model_lenght_graph1 <= 10:
            model_info_label1 = tk.Label(ui, text=((model_name)), bg="white")

        else:
            model_info_label1 = tk.Label(ui, text=((model_name[:10] + "...")), bg="white")

        model_info_label1.place(x=190, y=440, anchor='sw', )

        microturbulance_info_label1 = tk.Label(ui, text=(q_five_entry_input), bg="white")
        microturbulance_info_label1.place(x=190, y=477, anchor='sw', )

        loga_info_label1 = tk.Label(ui, text=((average_y_round_forgraph1)), bg="white")
        loga_info_label1.place(x=190, y=514, anchor='sw', )

        standardd_info_label1 = tk.Label(ui, text=(("± " + standard_deviation_y_forgraph1)), bg="white")
        standardd_info_label1.place(x=190, y=551, anchor='sw', )

        standarde_info_label1 = tk.Label(ui, text=(("± " + standard_error_str_forgraph1)), bg="white")
        standarde_info_label1.place(x=190, y=588, anchor='sw', )

        conflvl_info_label1 = tk.Label(ui, text=(("± " + confidence_level_str_forgraph1)), bg="white")
        conflvl_info_label1.place(x=190, y=625, anchor='sw', )

        elementh_info_label1 = tk.Label(ui, text=((solar_difference_result_forgraph1)), bg="white")
        elementh_info_label1.place(x=190, y=662, anchor='sw', )

        lineamount_info_label1 = tk.Label(ui, text=((b_forgraph1)), bg="white")
        lineamount_info_label1.place(x=190, y=699, anchor='sw', )

    if column_control == 2:

        model_info_label2.place_forget()
        loga_info_label2.place_forget()
        standardd_info_label2.place_forget()
        standarde_info_label2.place_forget()
        microturbulance_info_label2.place_forget()
        conflvl_info_label2.place_forget()
        elementh_info_label2.place_forget()
        lineamount_info_label2.place_forget()

        model_lenght_graph4 = len(model_name)
        if model_lenght_graph4 <= 10:
            model_info_label2 = tk.Label(ui, text=((model_name)), bg="white")

        else:
            model_info_label2 = tk.Label(ui, text=((model_name[:10] + "...")), bg="white")

        model_info_label2.place(x=300, y=440, anchor='sw', )

        microturbulance_info_label2 = tk.Label(ui, text=(q_five_entry_input), bg="white")
        microturbulance_info_label2.place(x=300, y=477, anchor='sw', )

        loga_info_label2 = tk.Label(ui, text=((average_y_round_forgraph4)), bg="white")
        loga_info_label2.place(x=300, y=514, anchor='sw', )

        standardd_info_label2 = tk.Label(ui, text=(("± " + standard_deviation_y_forgraph4)), bg="white")
        standardd_info_label2.place(x=300, y=551, anchor='sw', )

        standarde_info_label2 = tk.Label(ui, text=("± " + standard_error_str_forgraph4), bg="white")
        standarde_info_label2.place(x=300, y=588, anchor='sw', )

        conflvl_info_label2 = tk.Label(ui, text=(("± " + confidence_level_str_forgraph4)), bg="white")
        conflvl_info_label2.place(x=300, y=625, anchor='sw', )

        elementh_info_label2 = tk.Label(ui, text=((solar_difference_result_forgraph4)), bg="white")
        elementh_info_label2.place(x=300, y=662, anchor='sw', )

        lineamount_info_label4 = tk.Label(ui, text=((b_forgraph4)), bg="white")
        lineamount_info_label4.place(x=300, y=699, anchor='sw', )


# Creating the unprocessed panel

canvas = Canvas(ui, width=450, height=340)
canvas.create_rectangle(30, 40, 400, 340, fill="white")

canvas.create_line(290, 40, 290, 340, dash=(5, 2))

canvas.create_line(175, 40, 175, 340, dash=(5, 2))

canvas.place(x=0, y=710, anchor="sw")

selectfont = Font(size=9, weight="bold")

model_info_label1 = tk.Label(ui, text=("Model"), bg="white", font=selectfont)
model_info_label1.place(x=40, y=440, anchor='sw', )
model_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
model_info_label1.place(x=190, y=440, anchor='sw', )
model_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
model_info_label2.place(x=300, y=440, anchor='sw', )

microturbulance_info_label1 = tk.Label(ui, text=("Microturbulance"), bg="white", font=selectfont)
microturbulance_info_label1.place(x=40, y=477, anchor='sw', )
microturbulance_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
microturbulance_info_label1.place(x=190, y=477, anchor='sw', )
microturbulance_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
microturbulance_info_label2.place(x=300, y=477, anchor='sw', )

loga_info_label1 = tk.Label(ui, text=("log(A)"), bg="white", font=selectfont)
loga_info_label1.place(x=40, y=514, anchor='sw', )
loga_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
loga_info_label1.place(x=190, y=514, anchor='sw', )
loga_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
loga_info_label2.place(x=300, y=514, anchor='sw', )

standardd_info_label1 = tk.Label(ui, text=("Standard Deviation"), bg="white", font=selectfont)
standardd_info_label1.place(x=40, y=551, anchor='sw', )
standardd_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
standardd_info_label1.place(x=190, y=551, anchor='sw', )
standardd_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
standardd_info_label2.place(x=300, y=551, anchor='sw', )

standarde_info_label1 = tk.Label(ui, text=("Standard Error"), bg="white", font=selectfont)
standarde_info_label1.place(x=40, y=588, anchor='sw', )
standarde_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
standarde_info_label1.place(x=190, y=588, anchor='sw', )
standarde_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
standarde_info_label2.place(x=300, y=588, anchor='sw', )

conflvl_info_label1 = tk.Label(ui, text=("95% Confidence Level"), bg="white", font=selectfont)
conflvl_info_label1.place(x=40, y=625, anchor='sw', )
conflvl_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
conflvl_info_label1.place(x=190, y=625, anchor='sw', )
conflvl_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
conflvl_info_label2.place(x=300, y=625, anchor='sw', )

elementh_info_label1 = tk.Label(ui, text=("[Element/H]"), bg="white", font=selectfont)
elementh_info_label1.place(x=40, y=662, anchor='sw', )
elementh_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
elementh_info_label1.place(x=190, y=662, anchor='sw', )
elementh_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
elementh_info_label2.place(x=300, y=662, anchor='sw', )

lineamount_info_label1 = tk.Label(ui, text=("Number of Lines"), bg="white", font=selectfont)
lineamount_info_label1.place(x=40, y=699, anchor='sw', )
lineamount_info_label1 = tk.Label(ui, text=("<NONE>"), bg="white")
lineamount_info_label1.place(x=190, y=699, anchor='sw', )
lineamount_info_label2 = tk.Label(ui, text=("<NONE>"), bg="white")
lineamount_info_label2.place(x=300, y=699, anchor='sw', )

# Drawing empty graphs for the entrance screen


fig_1 = plt.figure(1, figsize=(4, 2.1))
graph_1 = fig_1.add_subplot(111)
graph_1.tick_params(labelsize=8)

plt.subplots_adjust(bottom=0.21)
plt.subplots_adjust(left=0.15)

plt.xlabel("Excitation Potential (eV)", fontsize=9)
plt.ylabel("log(A)", fontsize=9)
canvas = FigureCanvasTkAgg(fig_1, master=ui)
canvas.draw()
canvas.get_tk_widget().place(x=425, y=255, anchor="sw")

fig_2 = plt.figure(2, figsize=(4, 2.1))
graph_2 = fig_2.add_subplot(111)

plt.subplots_adjust(left=0.15)
graph_2.tick_params(labelsize=8)
plt.subplots_adjust(bottom=0.21)
plt.xlabel("Reduced E.W.", fontsize=9)
plt.ylabel("log(A)", fontsize=9)
canvas = FigureCanvasTkAgg(fig_2, master=ui)
canvas.draw()
canvas.get_tk_widget().place(x=425, y=480, anchor="sw")

fig_3 = plt.figure(3, figsize=(4, 2.1))
graph_3 = fig_3.add_subplot(111)

plt.subplots_adjust(left=0.15)
graph_3.tick_params(labelsize=8)
plt.subplots_adjust(bottom=0.21)
plt.xlabel("Wavelength (Å)", fontsize=9)
plt.ylabel("log(A)", fontsize=9)
canvas = FigureCanvasTkAgg(fig_3, master=ui)
canvas.draw()
canvas.get_tk_widget().place(x=425, y=705, anchor="sw")

fig_4 = plt.figure(4, figsize=(4, 2.1))
graph_4 = fig_4.add_subplot(111)

plt.subplots_adjust(left=0.15)
graph_4.tick_params(labelsize=8)
plt.subplots_adjust(bottom=0.21)
plt.xlabel("Excitation Potential (eV)", fontsize=9)
plt.ylabel("log(A)", fontsize=9)
canvas = FigureCanvasTkAgg(fig_4, master=ui)
canvas.draw()
canvas.get_tk_widget().place(x=850, y=255, anchor="sw")

fig_5 = plt.figure(5, figsize=(4, 2.1))
graph_5 = fig_5.add_subplot(111)

plt.subplots_adjust(left=0.15)
graph_5.tick_params(labelsize=8)
plt.subplots_adjust(bottom=0.21)
plt.xlabel("Reduced E.W.", fontsize=9)
plt.ylabel("log(A)", fontsize=9)
canvas = FigureCanvasTkAgg(fig_5, master=ui)
canvas.draw()
canvas.get_tk_widget().place(x=850, y=480, anchor="sw")

fig_6 = plt.figure(6, figsize=(4, 2.1))
graph_6 = fig_6.add_subplot(111)

plt.subplots_adjust(left=0.15)
graph_6.tick_params(labelsize=8)
plt.subplots_adjust(bottom=0.21)
plt.xlabel("Wavelength (Å)", fontsize=9)
plt.ylabel("log(A)", fontsize=9)
canvas = FigureCanvasTkAgg(fig_6, master=ui)
canvas.draw()
canvas.get_tk_widget().place(x=850, y=705, anchor="sw")

graphname_label1 = tk.Label(ui, text=("PANEL 1"), font=(15))
graphname_label2 = tk.Label(ui, text=("PANEL 2"), font=(15))

graphname_label1.place(x=600, y=40, anchor='sw')
graphname_label2.place(x=1020, y=40, anchor='sw')

# for the labels of what is selected

answer_label_4 = tk.Label(ui, text=("Selected --->   " + "NONE"))
answer_label_2 = tk.Label(ui, text=("Selected --->   " + "NONE"))
answer_label_1 = tk.Label(ui, text=("Selected --->   " + "NONE"))

answer_label_1.place(x=22, y=156, anchor='sw')
answer_label_2.place(x=22, y=218, anchor='sw')
answer_label_4.place(x=22, y=282, anchor='sw')

# for radio buttons

variable = IntVar()

radiobtn_ion1 = tk.Radiobutton(ui, text='Panel 1', variable=variable, value=1, command=radioselected_col1)
radiobtn_ion1.place(x=240, y=370, anchor='sw')

radiobtn_ion2 = tk.Radiobutton(ui, text='Panel 2', variable=variable, value=2, command=radioselected_col2)
radiobtn_ion2.place(x=330, y=370, anchor='sw')

# Creation of the checkbox
boxstatus = IntVar(0)
ionization_balance_btn = tk.Checkbutton(ui, text='Show ionization balance', variable=boxstatus,
                                        command=checkbox_decision)
ionization_balance_btn.place(x=240, y=400, anchor='sw')

# For info button

buttonfont = Font(size=13, weight="bold")
info_button = tk.Button(ui, text='ⓘ', height=1, width=3, font=buttonfont, command=open_info_screen)
info_button.place(x=200, y=55, anchor='sw')

# displaying question 1 and its button
q_one = tk.Label(ui, text=("Select the model:"), font=selectfont)
q_one.place(x=22, y=130, anchor='sw')

q_one_btn = tk.Button(ui, text='Select', height=2, width=20, command=openfile_q1)
q_one_btn.place(x=250, y=135, anchor='sw')

# displaying question 2 and its button
q_two = tk.Label(ui, text=("Select the line input file:"), font=selectfont)
q_two.place(x=22, y=190, anchor='sw')

q_two_btn = tk.Button(ui, text='Select', height=2, width=20, command=openfile_q2)
q_two_btn.place(x=250, y=197, anchor='sw')

# displaying question 3 and its button
q_three = tk.Label(ui, text=("Select the atom file:"), font=selectfont)
q_three.place(x=22, y=250, anchor='sw')

q_three_btn = tk.Button(ui, text='Select', height=2, width=20, command=openfile_q4)
q_three_btn.place(x=250, y=260, anchor='sw')

# displaying question 4 and its button
q_five = tk.Label(ui, text=("Enter microturbulance velocity:"), font=selectfont)
q_five.place(x=22, y=320, anchor='sw')

q_five_entry = tk.Entry(ui, width=18)
kmpers_label = tk.Label(ui, text=(" km/s"))
q_five_entry.place(x=250, y=320, anchor='sw')
kmpers_label.place(x=360, y=320, anchor='sw')

execute_btn = tk.Button(ui, text='Execute', height=3, width=25, command=mainprogram)
execute_btn.place(x=30, y=400, anchor='sw')

titlefont = Font(size=25, weight="bold", slant="italic")
titlefont2 = Font(size=10, slant="italic")

programname_label = tk.Label(ui, text='AbunCalc', font=titlefont)
programname_label.place(x=30, y=60, anchor='sw')

programname_label2 = tk.Label(ui, text='Abundance Analyzer for SPECTRUM Suite', font=titlefont2)
programname_label2.place(x=30, y=80, anchor='sw')


def on_close():
    close = messagebox.askokcancel("Close",
                                   "            REALLY WANT TO QUIT? \n\n --------------------------------------------------\n      AbunCalc version 1.0 ©, 2020 \n ------------------------------------------------- \n\n\n M. Taşkın Çay (mail@mail.com) \n                        & \n Aral Çay (mail@mail.com) \n\n                                   *** \n\n SPECTRUM suite © and Abundance © routine are property of \n Richard O. Gray (mail@mail.com) \n\n                                   *** \n\n If you use this program in your research, please give citation \n to the following papers: \n\n for AbunCalc: \n name of the paper, year, page, authors etc... \n\n for SPECTRUM and/or Abundance: \n name of the paper, year, page, authors etc...")
    if close:
        ui.destroy()
        sys.exit()


ui.protocol("WM_DELETE_WINDOW", on_close)

ui.mainloop()




