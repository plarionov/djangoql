
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionNAME DOT OR AND NOT IN TRUE FALSE NONE STRING_VALUE FLOAT_VALUE INT_VALUE PAREN_L PAREN_R EQUALS NOT_EQUALS GREATER GREATER_EQUAL LESS LESS_EQUAL CONTAINS NOT_CONTAINS\n        expression : PAREN_L expression PAREN_R\n        \n        expression : expression logical expression\n        \n        expression : name comparison_number number\n                   | name comparison_string string\n                   | name comparison_equality boolean_value\n                   | name comparison_equality none\n                   | name comparison_in_list const_list_value\n        \n        name : name_parts\n        \n        name_parts : name_parts DOT NAME\n                   | NAME\n        \n        logical : AND\n                | OR\n        \n        comparison_number : comparison_equality\n                          | comparison_greater_less\n        \n        comparison_string : comparison_equality\n                          | comparison_greater_less\n                          | comparison_contains\n        \n        comparison_equality : EQUALS\n                            | NOT_EQUALS\n        \n        comparison_greater_less : GREATER\n                                | GREATER_EQUAL\n                                | LESS\n                                | LESS_EQUAL\n        \n        comparison_contains : CONTAINS\n                            | NOT_CONTAINS\n        \n        comparison_in_list : IN\n                           | NOT IN\n        \n        const_value : number\n                    | string\n                    | none\n                    | boolean_value\n        \n        number : INT_VALUE\n               | FLOAT_VALUE\n        \n        string : STRING_VALUE\n        \n        none : NONE\n        \n        boolean_value : true\n                      | false\n        \n        true : TRUE\n        \n        false : FALSE\n        \n        const_list_value : PAREN_L const_value_list PAREN_R\n        \n        const_value_list : const_value_list const_value\n        \n        const_value_list : const_value\n        '
    
_lr_action_items = {'PAREN_L':([0,2,6,7,8,13,18,43,],[2,2,2,-11,-12,42,-26,-27,]),'NAME':([0,2,6,7,8,26,],[5,5,5,-11,-12,44,]),'$end':([1,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,51,],[0,-2,-1,-3,-32,-33,-4,-34,-5,-6,-36,-37,-35,-38,-39,-7,-40,]),'AND':([1,9,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,51,],[7,7,7,-1,-3,-32,-33,-4,-34,-5,-6,-36,-37,-35,-38,-39,-7,-40,]),'OR':([1,9,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,51,],[8,8,8,-1,-3,-32,-33,-4,-34,-5,-6,-36,-37,-35,-38,-39,-7,-40,]),'EQUALS':([3,4,5,44,],[16,-8,-10,-9,]),'NOT_EQUALS':([3,4,5,44,],[17,-8,-10,-9,]),'IN':([3,4,5,19,44,],[18,-8,-10,43,-9,]),'NOT':([3,4,5,44,],[19,-8,-10,-9,]),'GREATER':([3,4,5,44,],[20,-8,-10,-9,]),'GREATER_EQUAL':([3,4,5,44,],[21,-8,-10,-9,]),'LESS':([3,4,5,44,],[22,-8,-10,-9,]),'LESS_EQUAL':([3,4,5,44,],[23,-8,-10,-9,]),'CONTAINS':([3,4,5,44,],[24,-8,-10,-9,]),'NOT_CONTAINS':([3,4,5,44,],[25,-8,-10,-9,]),'DOT':([4,5,44,],[26,-10,-9,]),'PAREN_R':([9,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,45,46,47,48,49,50,51,52,],[28,-2,-1,-3,-32,-33,-4,-34,-5,-6,-36,-37,-35,-38,-39,-7,51,-42,-28,-29,-30,-31,-40,-41,]),'INT_VALUE':([10,12,14,16,17,20,21,22,23,30,31,33,36,37,38,39,40,42,45,46,47,48,49,50,52,],[30,-13,-14,-18,-19,-20,-21,-22,-23,-32,-33,-34,-36,-37,-35,-38,-39,30,30,-42,-28,-29,-30,-31,-41,]),'FLOAT_VALUE':([10,12,14,16,17,20,21,22,23,30,31,33,36,37,38,39,40,42,45,46,47,48,49,50,52,],[31,-13,-14,-18,-19,-20,-21,-22,-23,-32,-33,-34,-36,-37,-35,-38,-39,31,31,-42,-28,-29,-30,-31,-41,]),'STRING_VALUE':([11,12,14,15,16,17,20,21,22,23,24,25,30,31,33,36,37,38,39,40,42,45,46,47,48,49,50,52,],[33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-32,-33,-34,-36,-37,-35,-38,-39,33,33,-42,-28,-29,-30,-31,-41,]),'NONE':([12,16,17,30,31,33,36,37,38,39,40,42,45,46,47,48,49,50,52,],[38,-18,-19,-32,-33,-34,-36,-37,-35,-38,-39,38,38,-42,-28,-29,-30,-31,-41,]),'TRUE':([12,16,17,30,31,33,36,37,38,39,40,42,45,46,47,48,49,50,52,],[39,-18,-19,-32,-33,-34,-36,-37,-35,-38,-39,39,39,-42,-28,-29,-30,-31,-41,]),'FALSE':([12,16,17,30,31,33,36,37,38,39,40,42,45,46,47,48,49,50,52,],[40,-18,-19,-32,-33,-34,-36,-37,-35,-38,-39,40,40,-42,-28,-29,-30,-31,-41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,6,],[1,9,27,]),'name':([0,2,6,],[3,3,3,]),'name_parts':([0,2,6,],[4,4,4,]),'logical':([1,9,27,],[6,6,6,]),'comparison_number':([3,],[10,]),'comparison_string':([3,],[11,]),'comparison_equality':([3,],[12,]),'comparison_in_list':([3,],[13,]),'comparison_greater_less':([3,],[14,]),'comparison_contains':([3,],[15,]),'number':([10,42,45,],[29,47,47,]),'string':([11,42,45,],[32,48,48,]),'boolean_value':([12,42,45,],[34,50,50,]),'none':([12,42,45,],[35,49,49,]),'true':([12,42,45,],[36,36,36,]),'false':([12,42,45,],[37,37,37,]),'const_list_value':([13,],[41,]),'const_value_list':([42,],[45,]),'const_value':([42,45,],[46,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> PAREN_L expression PAREN_R','expression',3,'p_expression_parens','parser.py',28),
  ('expression -> expression logical expression','expression',3,'p_expression_logical','parser.py',34),
  ('expression -> name comparison_number number','expression',3,'p_expression_comparison','parser.py',40),
  ('expression -> name comparison_string string','expression',3,'p_expression_comparison','parser.py',41),
  ('expression -> name comparison_equality boolean_value','expression',3,'p_expression_comparison','parser.py',42),
  ('expression -> name comparison_equality none','expression',3,'p_expression_comparison','parser.py',43),
  ('expression -> name comparison_in_list const_list_value','expression',3,'p_expression_comparison','parser.py',44),
  ('name -> name_parts','name',1,'p_name','parser.py',50),
  ('name_parts -> name_parts DOT NAME','name_parts',3,'p_name_parts','parser.py',56),
  ('name_parts -> NAME','name_parts',1,'p_name_parts','parser.py',57),
  ('logical -> AND','logical',1,'p_logical','parser.py',66),
  ('logical -> OR','logical',1,'p_logical','parser.py',67),
  ('comparison_number -> comparison_equality','comparison_number',1,'p_comparison_number','parser.py',73),
  ('comparison_number -> comparison_greater_less','comparison_number',1,'p_comparison_number','parser.py',74),
  ('comparison_string -> comparison_equality','comparison_string',1,'p_comparison_string','parser.py',80),
  ('comparison_string -> comparison_greater_less','comparison_string',1,'p_comparison_string','parser.py',81),
  ('comparison_string -> comparison_contains','comparison_string',1,'p_comparison_string','parser.py',82),
  ('comparison_equality -> EQUALS','comparison_equality',1,'p_comparison_equality','parser.py',88),
  ('comparison_equality -> NOT_EQUALS','comparison_equality',1,'p_comparison_equality','parser.py',89),
  ('comparison_greater_less -> GREATER','comparison_greater_less',1,'p_comparison_greater_less','parser.py',95),
  ('comparison_greater_less -> GREATER_EQUAL','comparison_greater_less',1,'p_comparison_greater_less','parser.py',96),
  ('comparison_greater_less -> LESS','comparison_greater_less',1,'p_comparison_greater_less','parser.py',97),
  ('comparison_greater_less -> LESS_EQUAL','comparison_greater_less',1,'p_comparison_greater_less','parser.py',98),
  ('comparison_contains -> CONTAINS','comparison_contains',1,'p_comparison_contains','parser.py',104),
  ('comparison_contains -> NOT_CONTAINS','comparison_contains',1,'p_comparison_contains','parser.py',105),
  ('comparison_in_list -> IN','comparison_in_list',1,'p_comparison_in_list','parser.py',111),
  ('comparison_in_list -> NOT IN','comparison_in_list',2,'p_comparison_in_list','parser.py',112),
  ('const_value -> number','const_value',1,'p_const_value','parser.py',121),
  ('const_value -> string','const_value',1,'p_const_value','parser.py',122),
  ('const_value -> none','const_value',1,'p_const_value','parser.py',123),
  ('const_value -> boolean_value','const_value',1,'p_const_value','parser.py',124),
  ('number -> INT_VALUE','number',1,'p_number','parser.py',130),
  ('number -> FLOAT_VALUE','number',1,'p_number','parser.py',131),
  ('string -> STRING_VALUE','string',1,'p_string','parser.py',137),
  ('none -> NONE','none',1,'p_none','parser.py',147),
  ('boolean_value -> true','boolean_value',1,'p_boolean_value','parser.py',153),
  ('boolean_value -> false','boolean_value',1,'p_boolean_value','parser.py',154),
  ('true -> TRUE','true',1,'p_true','parser.py',160),
  ('false -> FALSE','false',1,'p_false','parser.py',166),
  ('const_list_value -> PAREN_L const_value_list PAREN_R','const_list_value',3,'p_const_list_value','parser.py',172),
  ('const_value_list -> const_value_list const_value','const_value_list',2,'p_const_value_list','parser.py',178),
  ('const_value_list -> const_value','const_value_list',1,'p_const_value_list_single','parser.py',184),
]