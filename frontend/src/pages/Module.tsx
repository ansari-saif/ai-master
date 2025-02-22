import React, { useEffect, useState } from 'react';
import ModuleItem from '../components/ModuleItem';
import { ModuleService, ModuleRead } from '../client';
import AddModuleForm from '@/components/AddModuleForm';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';

const Module: React.FC = () => {
  const [modules, setModule] = useState<ModuleRead[]>([]);
  const getModule = ()=>{
    ModuleService.listAllModuleApiV1ModuleGet()
      .then(setModule)
      .catch(console.error);
  }
  useEffect(() => {
    getModule()
  }, []);


  const handleDelete = (id: number) => {
    ModuleService.deleteModuleApiV1ModuleIdDelete({ moduleId: id })
      .then(() => {
        setModule((prev) => prev.filter((t) => t.id !== id));
      })
      .catch(console.error);
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-100 to-purple-100 p-8">
      <Link to="/" className="ml-4 bg-transparent border border-black px-6 py-3 rounded-md text-black hover:bg-white hover:text-indigo-600">
        Home
      </Link>
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="max-w-md mx-auto bg-white rounded-lg shadow-lg overflow-hidden"
      >
        <div className="p-6">
          <h1 className="text-3xl font-bold mb-6 text-center text-gray-800">Module</h1>
          <AddModuleForm onAdd={getModule} />
          <div className="mt-6 space-y-4">
            {modules.map((module) => (
              <motion.div
                key={module.id}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
                transition={{ duration: 0.3 }}
              >
                <ModuleItem
                  module={module}
                  onDelete={handleDelete}
                />
              </motion.div>
            ))}
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Module;
