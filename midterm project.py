MIN_TAW_NUM = 10
MIN_POSITIVE_VALUE = 1
box_count = 0
returned_boxes = 0
total_returned_taws = 0
accepted_taws = 0
box_with_1_lighter_taw = 0
box_with_1_heavier_taw = 0
box_with_equal_taw = 0
max_equal_taw_number = 0
the_heaviest_taw = 0
max_difference = 0
min_difference = 0
total_difference_lighter = 0
total_difference_heavier = 0
taw_weight_in_biggest_box = ' '
number_of_taws_in_the_box_with_heaviest_taw = ' '
percentage_of_the_largest_difference = 0
percentage_of_the_smallest_difference = 0
total_percentage_of_difference_light = 0
total_percentage_of_difference_heavy = 0

are_there_more_boxes = "y"
while are_there_more_boxes == "y" or are_there_more_boxes == "Y":
    box_count += 1
    percentage_of_difference = 0
    num_of_taws_in_a_box = int(input("How many taws are there in a box? "))
    manufacturing_defect = 0
    if num_of_taws_in_a_box >= MIN_TAW_NUM:
        dif_value = 0
        dif_value_counter = 0
        main_value = 0
        main_value_counter = 0
        remaining_taw = 0
        value = num_of_taws_in_a_box
        while num_of_taws_in_a_box > 0 and manufacturing_defect < 2:
            taw_weight = int(input("Weight of a taw: "))
            if taw_weight >= MIN_POSITIVE_VALUE:
                remaining_taw += 1
                if remaining_taw == 1:
                    main_value = taw_weight
                    main_value_counter += 1
                elif remaining_taw > 1:
                    if taw_weight != main_value and taw_weight != dif_value and dif_value != 0:
                        returned_boxes += 1
                        total_returned_taws += value
                        manufacturing_defect = 2
                        print("Detected a manufacturing defect.")
                    elif taw_weight != main_value and dif_value == 0:
                        dif_value = taw_weight
                        dif_value_counter += 1
                    elif taw_weight == main_value:
                        main_value = taw_weight
                        main_value_counter += 1
                    elif taw_weight != main_value and taw_weight == dif_value:
                        dif_value = taw_weight
                        dif_value_counter += 1
            else:
                print("The weight of a taw must be a positive value.")
                taw_weight = int(input("Weight of a taw: "))

            if dif_value_counter >= 2 and main_value_counter >= 2:
                total_returned_taws += value
                print("Detected a manufacturing defect.")
                returned_boxes += 1
                num_of_taws_in_a_box = 0

            elif num_of_taws_in_a_box == 1:
                accepted_taws += value
                if main_value_counter < dif_value_counter:
                    main_value, dif_value = dif_value, main_value
                if dif_value == 0:
                    dif_value = main_value
                difference_of_taw_weights = main_value - dif_value

                if difference_of_taw_weights > 0:
                    box_with_1_lighter_taw += 1
                    total_difference_lighter += difference_of_taw_weights
                    message = "One of the taw's weight is lighter than the others."
                    percentage_of_difference = 100 * difference_of_taw_weights / main_value
                    total_percentage_of_difference_light += percentage_of_difference
                    if difference_of_taw_weights > max_difference:
                        max_difference = difference_of_taw_weights
                        percentage_of_the_largest_difference = 100 * max_difference / main_value
                        sign_max = "Light"
                    if min_difference == 0:
                        min_difference = main_value
                        if difference_of_taw_weights < min_difference:
                            min_difference = difference_of_taw_weights
                            final_min_difference = min_difference
                            percentage_of_the_smallest_difference = 100 * final_min_difference / main_value
                            sign_min = "Light"
                    elif difference_of_taw_weights < min_difference:
                        min_difference = difference_of_taw_weights
                        final_min_difference = min_difference
                        percentage_of_the_smallest_difference = 100 * final_min_difference / main_value
                        sign_min = "Light"
                elif difference_of_taw_weights < 0:
                    difference_of_taw_weights = abs(difference_of_taw_weights)
                    total_difference_heavier += difference_of_taw_weights
                    box_with_1_heavier_taw += 1
                    message = "One of the taw's weight is heavier than the others."
                    percentage_of_difference = difference_of_taw_weights / main_value * 100
                    total_percentage_of_difference_heavy += percentage_of_difference
                    if difference_of_taw_weights > max_difference:
                        max_difference = difference_of_taw_weights
                        percentage_of_the_largest_difference = 100 * max_difference / main_value
                        sign_max = "Heavy"
                    if min_difference == 0:
                        min_difference = dif_value
                        if difference_of_taw_weights < min_difference:
                            min_difference = difference_of_taw_weights
                            final_min_difference = min_difference
                            percentage_of_the_smallest_difference = 100 * final_min_difference / main_value
                            sign_min = "Heavy"
                    elif difference_of_taw_weights < min_difference:
                        min_difference = difference_of_taw_weights
                        final_min_difference = min_difference
                        percentage_of_the_smallest_difference = 100 * final_min_difference / main_value
                        sign_min = "Heavy"
                else:
                    box_with_equal_taw += 1
                    message = "Weight of all taws are equal."
                    if value > max_equal_taw_number:
                        max_equal_taw_number = value
                        taw_weight_in_biggest_box = main_value
                    if main_value > the_heaviest_taw:
                        the_heaviest_taw = main_value
                        number_of_taws_in_the_box_with_heaviest_taw = value

                print(f"{message}"
                      f"\nValue of difference: {difference_of_taw_weights} mg"
                      f"\nThe percentage of weight difference: {round(percentage_of_difference ,2)}%")
            num_of_taws_in_a_box -= 1

    are_there_more_boxes = input("Are there any more boxes? (y, Y, n, N)  ")

percentage_for_manufacturing_defects = returned_boxes / box_count * 100
accepted_boxes = box_count - returned_boxes
percentage_of_boxes_with_equal_taw_weights = box_with_equal_taw / accepted_boxes * 100
percentage_of_boxes_with_1_heavier_taw = box_with_1_heavier_taw / accepted_boxes * 100
percentage_of_boxes_with_1_lighter_taw = box_with_1_lighter_taw / accepted_boxes * 100
average_weight_difference_heavy = total_difference_heavier / box_with_1_heavier_taw
average_weight_difference_light = total_difference_lighter / box_with_1_lighter_taw
average_of_total_percent_difference_heavy = total_percentage_of_difference_heavy / box_with_1_heavier_taw
average_of_total_percent_difference_light = total_percentage_of_difference_light / box_with_1_lighter_taw

print(f"Number of boxes with manufacturing defects: {returned_boxes}, "
      f"their percentages in all boxes: {round(percentage_for_manufacturing_defects ,2)}%"
      f"\nNumber of taws returned: {total_returned_taws}"
      f"\nNumber of taws accepted: {accepted_taws}"
      f"\nNumber of boxes in which all taws are of equal weight: {box_with_equal_taw}, "
      f"percentages in boxes without manufacturing defects: {round(percentage_of_boxes_with_equal_taw_weights ,2)}%"
      f"\nNumber of boxes in which 1 taw is heavier than the others: {box_with_1_heavier_taw}, "
      f"percentages in boxes without manufacturing defects: {round(percentage_of_boxes_with_1_heavier_taw ,2)}%"
      f"\nNumber of boxes in which 1 taw is lighter than the others: {box_with_1_lighter_taw}, "
      f"percentages in boxes without manufacturing defects: {round(percentage_of_boxes_with_1_lighter_taw ,2)}%"
      f"\nAverage of weight difference values in boxes where 1 taw is heavier "
      f"than the others: {round(average_weight_difference_heavy ,2)}"
      f"\nAverage of weight difference percentages of the heavier taws in boxes where 1 taw is heavier "
      f"than the others: {round(average_of_total_percent_difference_heavy ,2)}"
      f"\nAverage of weight difference values in boxes where 1 taw is lighter "
      f"than the others: {round(average_weight_difference_light ,2)}"
      f"\nAverage of weight difference percentages of the lighter taws in boxes where 1 taw is lighter "
      f"than the others: {round(average_of_total_percent_difference_light ,2)}"
      f"\nAmong the boxes in which all taws are of equal weight; "
      f"\n    The number of taws in the box with the largest number of taws: {max_equal_taw_number},"
      f"\n    The weight of 1 taw in that box: {taw_weight_in_biggest_box} mg"
      f"\n    The number of taws in the box with the heaviest taws: {number_of_taws_in_the_box_with_heaviest_taw}, "
      f"\n    The weight of 1 taw in that box: {the_heaviest_taw} mg"
      f"\nWhen the difference between the weight of the different taw and the weight of the other taws in "
      f"the box is the largest;"
      f"\n    Value: {max_difference} mg"
      f"\n    Percentage: {round(percentage_of_the_largest_difference ,2)}%"
      f"\n    Sign: {sign_max}"
      f"\nWhen the difference between the weight of the different taw and the weight of the other taws in "
      f"the box is the smallest;"
      f"\n    Value: {final_min_difference} mg"
      f"\n    Percentage: {round(percentage_of_the_smallest_difference ,2)}%"
      f"\n    Sign: {sign_min}")
