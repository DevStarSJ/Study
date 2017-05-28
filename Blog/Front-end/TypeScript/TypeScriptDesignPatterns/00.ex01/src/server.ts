export class Server {
    store: DataStore = {
        timestamp: 0,
        data: ""
    };

    getData(clientTimeStamp: number): DataStore {
        if (clientTimeStamp < this.store.timestamp) {
            return {
                timestamp: this.store.timestamp,
                data: this.store.data
            };
        } else {
            return undefined;
        }
    }

    synchronize(clientDataStore: DataStore): DataStore {
        if (clientDataStore.timestamp > this.store.timestamp) {
            this.store = clientDataStore;
            return undefined;
        } else if (clientDataStore.timestamp < this.store.timestamp) {
            return this.store;
        } else {
            return undefined;
        }
    }
}

export interface DataStore {
    timestamp: number;
    data: string;
}

interface DataSyncingInfo {
    timestamp: number;
    data: string;
}
