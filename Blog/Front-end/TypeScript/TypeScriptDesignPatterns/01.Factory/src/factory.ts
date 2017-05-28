class Payload {
    constructor(public weight: number) { }
}

class Engine {
    constructor(public thrust: number) {}
}

class Stage {
    constructor(public engines: Engine[]) {}
}

class Rocket {
    payload: Payload;
    stages: Stage[];
}

class RocketFactory {
    buildRocket(): Rocket { 
        let rocket = new Rocket();
        rocket.payload = this.createPayload();
        rocket.stages = this.createStages();
        return rocket;
        
    }

    createPayload(): Payload { 
        return new Payload(0);
     }

    createStages(): Stage[] {
        let engine = new Engine(1000);
        let stage = new Stage([engine]);
        return [stage];
    }
}

let rocketFactory = new RocketFactory();
let rocket = rocketFactory.buildRocket();

console.info(JSON.stringify(rocket));

//-------------

class Satellite extends Payload {
    constructor(public id: number) {
        super(200);
    }
}

class FirstStage extends Stage {
    constructor() {
        super([
            new Engine(1000),new Engine(1000),new Engine(1000),new Engine(1000)
        ]);
    }
}

class SecondStage extends Stage {
    constructor() {
        super([new Engine(1000)]);
    }
}

type FreightRocketStages = [FirstStage, SecondStage];

class FreightRocketFactory extends RocketFactory {
    nextSatelliteId = 0;

    createPayload(): Satellite {
        return new Satellite(this.nextSatelliteId++);
    }

    createStages(): FreightRocketStages {
        return [new FirstStage(), new SecondStage()];
    }
}

let freightRocketFactory = new FreightRocketFactory();
let rocket2 = freightRocketFactory.buildRocket();
let rocket3 = freightRocketFactory.buildRocket();
console.info(JSON.stringify(rocket2));
console.info(JSON.stringify(rocket3));
