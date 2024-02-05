# # 33.	Write a program to get the Pascale’s triangle
#under testing updated soon
# -----------------------------
# def generate_pascals_triangle(num_rows):
#     triangle = []

#     for i in range(num_rows):
#         row = [None] * (i + 1)
#         row[0], row[-1] = 1, 1  # First and last elements of each row are always 1

#         for j in range(1, len(row) - 1):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

#         triangle.append(row)

#     return triangle

# def print_pascals_triangle(triangle):
#     for row in triangle:
#         for element in row:
#             print(element, end=" ")
#         print()  

# num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
# pascals_triangle = generate_pascals_triangle(num_rows)
# print("Pascal's Triangle:")
# print_pascals_triangle(pascals_triangle)
