from factories import loader

factory = loader.load_factory('extract_factory')
print(factory)

#process = factory.start_process()
#
#process.connect()
#process.extract()
#
#
#
#factory = loader.load_factory('transform_factory')
#print(factory)
#
#process = factory.start_process()
#
#process.transfor_process_1()
#process.transfor_process_2()
#
#
#
#factory = loader.load_factory('load_factory')
#print(factory)