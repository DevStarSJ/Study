interface Storage {
    get<T>(key:string):Promise<T>;
    set<T>(key:string, value:T):Promise<void>;
}

class IndexedDBStorage implements Storage {
    constructor(
        public db: IDBDatabase,
        public storeName = "default"
    ) {}

}