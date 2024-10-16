import React, { useState } from 'react';
import { DefaultService, TodoCreate } from '../client';
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
interface AddTodoFormProps {
  onAdd: (newTodo: TodoCreate) => void;
}

const AddTodoForm: React.FC<AddTodoFormProps> = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const newTodo: TodoCreate = {
      title,
      description,
    };

    DefaultService.createTodoApiV1TodosPost({ requestBody: newTodo })
      .then(onAdd)
      .catch(console.error);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <Input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          className="w-full"
        />
      </div>
      <div>
        <Textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full"
        />
      </div>
      <Button type="submit" className="w-full">Add Todo</Button>
    </form>
  );
};

export default AddTodoForm;
