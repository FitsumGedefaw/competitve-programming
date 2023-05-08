class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for i in range(n):
            recipe, ingr = recipes[i], ingredients[i]
            
            for ingred in ingr:
                graph[ingred].append(recipe)
                incoming[recipe] += 1
            
        queue = deque(supplies)
        doableMeals = []
                
        while queue:
            item = queue.popleft()
            
            if item in recipes:
                doableMeals.append(item)
            
            for neighbour in graph[item]:
                incoming[neighbour] -= 1
                
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
                    
        return doableMeals
        
        
                    
            
                
            
        