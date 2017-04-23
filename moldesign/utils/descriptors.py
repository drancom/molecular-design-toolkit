# Copyright 2016 Autodesk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Alias(object):
    """
    Descriptor that calls a child object's method.
    e.g.
    >>> class A(object):
    >>>     childkeys = Alias('child.keys')
    >>>     child = dict()
    >>>
    >>> a = A()
    >>> a.child['key'] = 'value'
    >>> a.childkeys() #calls a.child.keys(), returns ['key']
    ['key']
    """
    def __init__(self, objmethod):
        objname, methodname = objmethod.split('.')
        self.objname = objname
        self.methodname = methodname

    def __get__(self, instance, owner):
        proxied = getattr(instance, self.objname)
        return getattr(proxied,self.methodname)


class Synonym(object):
    """ An attribute (class or intance) that is just a synonym for another.
    """
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Attribute(object):
    """For overriding a property in a superclass - turns the attribute back
    into a normal instance attribute"""
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        return setattr(instance, self.name, value)
