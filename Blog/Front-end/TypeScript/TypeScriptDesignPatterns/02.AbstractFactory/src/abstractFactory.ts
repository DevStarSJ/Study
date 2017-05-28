class Engine {
    constructor(public thrust: number) {}
}

interface Payload {
    weight: number;
}

interface Stage {
    engines: Engine[];
}

interface Rocket {
    payload: Payload;
    stages: Stage[];
}

interface RocketFactory<T extends Rocket> {
    createRocket(): T;
    createPayload(): Payload;
    createStages(): Stage[];
}

class Client {
    buildRocket<T extends Rocket>(factory: RocketFactory<T>): T {
        let rocket = factory.createRocket();
        rocket.payload = factory.createPayload();
        rocket.stages = factory.createStages();
        return rocket;
    }
}

class ExperimentalPayload implements Payload {
    weight: number;
}

class ExperimentalRocketStage implements Stage {
    engines: Engine[];
}

class ExperimentalRocket implements Rocket {
    payload: ExperimentalPayload;
    stages: ExperimentalRocketStage[];
}

class ExperimentalRocketFactory implements RocketFactory<ExperimentalRocket> {
    createRocket(): ExperimentalRocket {
        return new ExperimentalRocket();
    }
    createPayload(): ExperimentalPayload {
        return new ExperimentalPayload();
    }
    createStages(): ExperimentalRocketStage[] {
        return [new ExperimentalRocketStage()];
    }
}

let client = new Client();
let factory = new ExperimentalRocketFactory();
let rocket = client.buildRocket(factory);
console.info(rocket);

class Satellite implements Payload {
    constructor (
        public id: number,
        public weight: number
    ) {}
}

class FreightRocketFirstStage implements Stage {
    engines: Engine[];
}

class FreightRocketSecondStage implements Stage {
    engines: Engine[];
}

type FreightRocketStages = [FreightRocketFirstStage, FreightRocketSecondStage];

class FreightRocket implements Rocket {
    payload: Satellite;
    stages: FreightRocketStages;
}

class FreightRocketFactory implements RocketFactory<FreightRocket> {
    nextSatelliteId = 0;
    createRocket(): FreightRocket {
        return new FreightRocket();
    }
    createPayload(): Payload {
        return new Satellite(this.nextSatelliteId++, 100);
    }
    createStages(): Stage[] {
        return [new FreightRocketFirstStage(), new FreightRocketSecondStage()];
    }
}

let client2 = new Client();

let experimentalRocketFactory = new ExperimentalRocketFactory();
let freightRocketFactory = new FreightRocketFactory();

let experimentalRocket = client2.buildRocket(experimentalRocketFactory);
let freightRocket = client2.buildRocket(freightRocketFactory);

console.info(experimentalRocket);
console.info(freightRocket);
