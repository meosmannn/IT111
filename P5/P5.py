def make_table(row, col, header=False):
    col_count = 0
    row_count = 0
  
    print("<table>")
    
    if header:
        print("<tr>")
        for _ in range(col):
            print("<th>Header</th>")
        print("</tr>")
  
    while row_count < row:
        print("<tr>")
        while col_count < col:
            print("<td>Cell</td>")
            col_count += 1
        print("</tr>")
        row_count += 1
        col_count = 0
     
    print("</table>")

make_table(2, 3, True)
