#coding=utf-8

#打开一个文件
fo = open("/opt/work/ef/docs/策划/2.4.0/tpl_localization(多语言表).xlsx","r+")

# print "fileName: ", fo.name
# print "is closed: ", fo.closed
# print "mode: ", fo.mode
# print "lllll: ", fo.softspace

print fo.read(1024)

fo.close()

