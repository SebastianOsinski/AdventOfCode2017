class Program:

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def total_weight(self):
        return self.weight + sum([child.total_weight() for child in self.children])

    def find_correct_weight_for_wrongly_weighted_program(self, correct_weight):
        children_with_weight = {}
        for i in range(0, len(self.children)):
            weight = self.children[i].total_weight()

            if weight in children_with_weight:
                children_with_weight[weight].append(self.children[i])
            else:
                children_with_weight[weight] = [self.children[i]]

        wrong_child = None
        children_weight_sum = 0
        correct_child_weight = 0
        for weight in children_with_weight:
            children_weight_sum += weight * len(children_with_weight[weight])
            if len(children_with_weight[weight]) == 1:
                wrong_child = children_with_weight[weight][0]
            else:
                correct_child_weight = weight

        # if no child is wrong then current program is problem
        if wrong_child is None:
            diff = self.weight + children_weight_sum - correct_weight
            return self.weight - diff
        else:
            return wrong_child.find_correct_weight_for_wrongly_weighted_program(correct_child_weight)





