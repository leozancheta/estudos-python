from facade import ImplementsNumpy

data = [1, 2, 3, 4, 5]
numpy_impl = ImplementsNumpy()
array = numpy_impl.criar_array(data)
print("Array:", array)
print("Média:", numpy_impl.media(array))
print("Desvio Padrão:", numpy_impl.desvio_padrao(array))
print("Soma:", numpy_impl.soma(array))