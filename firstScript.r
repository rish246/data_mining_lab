vector.one <- c(1, 3);

get.max <- function(listElements) {
	max.element <- 0

	for( i in 1:length(listElements) ) {
		if( listElements[i] > max.element ) {
			max.element <- listElements[i];
		}

	}	
	
	max.element
}


list.elements <- c(1, 3, 2, 5, 2, 9, 7);

max.element <- get.max(list.elements);

print("Max element in the list is = ", max.element);

print(vector.one[1]);
