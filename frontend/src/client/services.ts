import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { TodoCreate,TodoRead,TodoUpdateSchema,PatientCreate,PatientRead } from './models';

export type TodoData = {
        CreateTodoApiV1TodoPost: {
                    requestBody: TodoCreate
                    
                };
GetTodoApiV1TodoTodoIdGet: {
                    todoId: number
                    
                };
UpdateTodoApiV1TodoTodoIdPut: {
                    requestBody: TodoUpdateSchema
todoId: number
                    
                };
DeleteTodoApiV1TodoTodoIdDelete: {
                    todoId: number
                    
                };
    }

export type PatientData = {
        CreatePatientApiV1PatientPost: {
                    requestBody: PatientCreate
                    
                };
    }

export class TodoService {

	/**
	 * List All Todo
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static listAllTodoApiV1TodoGet(): CancelablePromise<Array<TodoRead>> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/todo/',
		});
	}

	/**
	 * Create Todo
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static createTodoApiV1TodoPost(data: TodoData['CreateTodoApiV1TodoPost']): CancelablePromise<TodoRead> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/todo/',
			body: requestBody,
			mediaType: 'application/json',
		});
	}

	/**
	 * Get Todo
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static getTodoApiV1TodoTodoIdGet(data: TodoData['GetTodoApiV1TodoTodoIdGet']): CancelablePromise<TodoRead> {
		const {
todoId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/todo/{todo_id}',
			path: {
				todo_id: todoId
			},
		});
	}

	/**
	 * Update Todo
	 * @returns TodoRead Successful Response
	 * @throws ApiError
	 */
	public static updateTodoApiV1TodoTodoIdPut(data: TodoData['UpdateTodoApiV1TodoTodoIdPut']): CancelablePromise<TodoRead> {
		const {
todoId,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/todo/{todo_id}',
			path: {
				todo_id: todoId
			},
			body: requestBody,
			mediaType: 'application/json',
		});
	}

	/**
	 * Delete Todo
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static deleteTodoApiV1TodoTodoIdDelete(data: TodoData['DeleteTodoApiV1TodoTodoIdDelete']): CancelablePromise<Record<string, unknown>> {
		const {
todoId,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/todo/{todo_id}',
			path: {
				todo_id: todoId
			},
		});
	}

}

export class PatientService {

	/**
	 * List All Patient
	 * @returns PatientRead Successful Response
	 * @throws ApiError
	 */
	public static listAllPatientApiV1PatientGet(): CancelablePromise<Array<PatientRead>> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/patient/',
		});
	}

	/**
	 * Create Patient
	 * @returns PatientRead Successful Response
	 * @throws ApiError
	 */
	public static createPatientApiV1PatientPost(data: PatientData['CreatePatientApiV1PatientPost']): CancelablePromise<PatientRead> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/patient/',
			body: requestBody,
			mediaType: 'application/json',
		});
	}

}