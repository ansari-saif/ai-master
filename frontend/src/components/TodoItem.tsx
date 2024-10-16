import React from 'react';
import { TodoRead } from '../client';
import { Checkbox } from "@/components/ui/checkbox"
import { Button } from "@/components/ui/button"
import { Trash2 } from "lucide-react"

interface TodoItemProps {
  todo: TodoRead;
  onToggle: (id: number) => void;
  onDelete: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete }) => {
  return (
    <div className="flex items-start space-x-4 p-4 bg-card rounded-lg shadow">
    <Checkbox
      id={`todo-${todo.id}`}
      checked={todo.is_completed}
      onCheckedChange={() => onToggle(todo.id)}
    />
    <div className="flex-grow">
      <h3 className="text-lg font-semibold leading-none tracking-tight">
        {todo.title}
      </h3>
      <p className="text-sm text-muted-foreground mt-1">{todo.description}</p>
    </div>
    <Button
      variant="destructive"
      size="icon"
      onClick={() => onDelete(todo.id)}
      aria-label="Delete todo"
    >
      <Trash2 className="h-4 w-4" />
    </Button>
  </div>
  );
};

export default TodoItem;
