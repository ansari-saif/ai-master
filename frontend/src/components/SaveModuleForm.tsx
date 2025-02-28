import React, { useState, useEffect } from 'react';
import { ModuleCreate, ModuleRead, ModuleService } from '../client';



interface SaveModuleFormProps {
  onSave: () => void;
  editModule: ModuleCreate;
}

const SaveModuleForm: React.FC<SaveModuleFormProps> = ({ onSave, editModule }) => {
  const [formData, setFormData] = useState<ModuleCreate>({
    title: editModule.title,
    description: editModule.description
  });
  const isEditing = !!(editModule as ModuleRead)?.id;

  useEffect(() => {
    setFormData({
      title: editModule.title || '',
      description: editModule.description || ''
    });
  }, [editModule]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.title.trim()) return;

    if (isEditing) {
      ModuleService.updateModuleApiV1ModuleIdPut({
        moduleId: (editModule as ModuleRead).id,
        requestBody: formData
      })
        .then(() => {
          setFormData({ title: '', description: '' });
          onSave();
        })
        .catch(console.error);
    } else {
      ModuleService.createModuleApiV1ModulePost({ requestBody: formData })
        .then(() => {
          setFormData({ title: '', description: '' });
          onSave();
        })
        .catch(console.error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4">
      <div className="flex flex-col pd-5 m-5 space-y-4">
        <label htmlFor="title" className="text-gray-700">Title</label>
        <input
          id="title"
          name="title"
          type="text"
          value={formData.title}
          onChange={handleChange}
          placeholder="Title"
          className="w-full px-4 py-2 text-gray-700 bg-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
        />
      </div>
      <div className="flex flex-col pd-5 m-5 space-y-4">
        <label htmlFor="description" className="text-gray-700">Description</label>
        <input
          id="description"
          name="description"
          type="text"
          value={formData.description}
          onChange={handleChange}
          placeholder="Description"
          className="w-full px-4 py-2 text-gray-700 bg-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
        />
      </div>
      <div className="flex justify-end">
        <button
          type="submit"
          className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
        >
          Save
        </button>
      </div>
    </form>
  );
};

export default SaveModuleForm;
