number_of_pens = int(input())
number_of_markers = int(input())
liters_of_thinner = int(input())
percent_discount = int(input())
discount = percent_discount / 100

package_pens = 5.80
package_markers = 7.20
thinner_per_liter = 1.20

order = (number_of_pens * package_pens) + (number_of_markers * package_markers) + (liters_of_thinner * thinner_per_liter)
discount_order = order - (order * discount)
print(discount_order)
