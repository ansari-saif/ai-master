import React, { useState, useEffect } from "react";
import { ModuleCreate, ModuleRead, ModuleService } from "../client";

interface SaveModuleFormProps {
  onSave: () => void;
  editModule: ModuleCreate | ModuleRead;
}

const SaveModuleForm: React.FC<SaveModuleFormProps> = ({ onSave, editModule }) => {
  const isEditing = "id" in editModule;

  const [formData, setFormData] = useState<ModuleCreate>({
    title: editModule.title || "",
    description: editModule.description || "",
  });

  useEffect(() => {
    setFormData({
      title: editModule.title || "",
      description: editModule.description || "",
    });
  }, [editModule]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.title.trim()) return;

    try {
      if (isEditing) {
        await ModuleService.updateModuleApiV1ModuleIdPut({
          moduleId: (editModule as ModuleRead).id,
          requestBody: formData,
        });
      } else {
        await ModuleService.createModuleApiV1ModulePost({ requestBody: formData });
      }

      setFormData({ title: "", description: "" });
      onSave();
    } catch (error) {
      console.error("Error saving module:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4 space-y-4">
      {["title", "description"].map((field) => (
        <div key={field} className="flex flex-col px-5 py-2 space-y-2">
          <label htmlFor={field} className="text-gray-700 capitalize">
            {field}
          </label>
          <input
            id={field}
            name={field}
            type="text"
            value={formData[field as keyof ModuleCreate]}
            onChange={handleChange}
            placeholder={field}
            className="w-full px-4 py-2 text-gray-700 bg-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-300 ease-in-out"
          />
        </div>
      ))}
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
