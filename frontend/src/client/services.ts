import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { ModuleCreate,ModuleRead,ModuleUpdate } from './models';

export type ModuleData = {
        CreateModuleApiV1ModulePost: {
                    requestBody: ModuleCreate
                    
                };
GetModuleApiV1ModuleIdGet: {
                    moduleId: number
                    
                };
UpdateModuleApiV1ModuleIdPut: {
                    moduleId: number
requestBody: ModuleUpdate
                    
                };
DeleteModuleApiV1ModuleIdDelete: {
                    moduleId: number
                    
                };
    }

export class ModuleService {

	/**
	 * List All Module
	 * @returns ModuleRead Successful Response
	 * @throws ApiError
	 */
	public static listAllModuleApiV1ModuleGet(): CancelablePromise<Array<ModuleRead>> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/module/',
		});
	}

	/**
	 * Create Module
	 * @returns ModuleRead Successful Response
	 * @throws ApiError
	 */
	public static createModuleApiV1ModulePost(data: ModuleData['CreateModuleApiV1ModulePost']): CancelablePromise<ModuleRead> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/module/',
			body: requestBody,
			mediaType: 'application/json',
		});
	}

	/**
	 * Get a single Module
	 * @returns ModuleRead Successful Response
	 * @throws ApiError
	 */
	public static getModuleApiV1ModuleIdGet(data: ModuleData['GetModuleApiV1ModuleIdGet']): CancelablePromise<ModuleRead> {
		const {
moduleId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/module/{module_id}',
			path: {
				module_id: moduleId
			},
		});
	}

	/**
	 * Update a Module
	 * @returns ModuleRead Successful Response
	 * @throws ApiError
	 */
	public static updateModuleApiV1ModuleIdPut(data: ModuleData['UpdateModuleApiV1ModuleIdPut']): CancelablePromise<ModuleRead> {
		const {
moduleId,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/module/{module_id}',
			path: {
				module_id: moduleId
			},
			body: requestBody,
			mediaType: 'application/json',
		});
	}

	/**
	 * Delete a Module
	 * @returns void No Content
	 * @throws ApiError
	 */
	public static deleteModuleApiV1ModuleIdDelete(data: ModuleData['DeleteModuleApiV1ModuleIdDelete']): CancelablePromise<void> {
		const {
moduleId,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/module/{module_id}',
			path: {
				module_id: moduleId
			},
		});
	}

}