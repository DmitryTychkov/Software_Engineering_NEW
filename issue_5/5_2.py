result_of_run = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
                 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sort_result = sorted(result_of_run)
sort_result_reverse = sorted(result_of_run, reverse=True)

print("Лучшие результаты: ", sort_result[0], sort_result[1], sort_result[2])
print("Худшие результаты: ", sort_result_reverse[0], sort_result_reverse[1], sort_result_reverse[2])
print("Все результаты начиная с 10: ", sort_result)