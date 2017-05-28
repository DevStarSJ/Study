interface Payload {
    weight: number;
}

class Engine {
    constructor(public thrust: number) {}
}

interface Stage {
    engines: Engine[];
}

interface Rocket {
    payload: Payload;
}

class Probe implements Payload {
    weight: number;
}

class SolidRocketEngine extends Engine {}

class SoundingRocket implements Rocket {
    payload: Probe;
    engine: SolidRocketEngine;
}

class LiquidRocketEngine extends Engine {
    fuelLevel = 0;
    refuel(level: number): void {
        this.fuelLevel = level;
    }
}

abstract class LiquidRocketStage implements Stage {
    engines: LiquidRocketEngine[] = [];
    refuel(level = 100): void {
        for (let engine of this.engines) {
            engine.refuel(level);
        }
    }
}

class FreightRocketFirstStage extends LiquidRocketStage {
    constructor(thrust: number) {
        super();
        let enginesNumber = 4;
        let singleEngineThrust = thrust / enginesNumber;
        for (let i = 0; i < enginesNumber; i++) {
            let engine = new LiquidRocketEngine(singleEngineThrust);
            this.engines.push(engine);
        }
    }
}

class FreightRocketSecondStage extends LiquidRocketStage {
    constructor(thrust: number) {
        super();
        this.engines.push(new LiquidRocketEngine(thrust));
    }
}

class Satellite implements Payload {
    constructor (
        public id: number,
        public weight: number
    ) {}
}

type FreightRocketStages = [FreightRocketFirstStage, FreightRocketSecondStage];

class FreightRocket implements Rocket {
    payload: Satellite;
    stages : FreightRocketStages = [new FreightRocketFirstStage(0), new FreightRocketSecondStage(0)];
}

abstract class RocketBuilder<TRocket extends Rocket, TPayload extends Payload> {
    createRocket(): void {}
    addPayload(payload: TPayload): void {}
    addStages(): void {}
    refuelRocket(): void {}
    abstract get rocket(): TRocket;
}

class Director {
    prepareRocket<TRocket extends Rocket, TPayload extends Payload>
    (builder: RocketBuilder<TRocket, TPayload>, payload: TPayload): TRocket {
        builder.createRocket();
        builder.addPayload(payload);
        builder.addStages();
        builder.refuelRocket();
        return builder.rocket;
    }
}

class SoundingRocketBuilder extends RocketBuilder<SoundingRocket, Probe> {
    private buildingRocket: SoundingRocket;

    createRocket(): void {
        this.buildingRocket = new SoundingRocket();
    }

    addPayload(probe: Probe): void {
        this.buildingRocket.payload = probe;
    }

    addStages(): void {
        let payload = this.buildingRocket.payload;
        this.buildingRocket.engine = new SolidRocketEngine(payload.weight);
    }

    get rocket(): SoundingRocket {
        return this.buildingRocket;
    }
}

class FreightRocketBuilder extends RocketBuilder<FreightRocket, Satellite> {
    private buildingRocket: FreightRocket;

    createRocket(): void {
        this.buildingRocket = new FreightRocket();
    }

    addPayload(satellite: Satellite): void {
        this.buildingRocket.payload = satellite;
    }

    get rocket(): FreightRocket {
        return this.buildingRocket;
    }

    static oneStageMax = 1000;

    addStages(): void {
        let rocket = this.buildingRocket;
        let payload = rocket.payload;
        let stages = rocket.stages;
        console.info(rocket);

        stages[0] = new FreightRocketFirstStage(payload.weight * 4);
        if (payload.weight >= FreightRocketBuilder.oneStageMax) {
            stages[1] = new FreightRocketSecondStage(payload.weight);
        }
    }

    static twoStagesMax = 2000;
    refuel(): void {
        let rocket = this.buildingRocket;
        let payload = rocket.payload;
        let stages = rocket.stages;
        let oneMax = FreightRocketBuilder.oneStageMax;
        let twoMax = FreightRocketBuilder.twoStagesMax;
        let weight = payload.weight;

        stages[0].refuel(Math.min(weight, oneMax) / oneMax * 100);
        if (weight >= oneMax) {
            stages[1].refuel((weight-oneMax)/(twoMax-oneMax)*100);
        }
    }
}

let director = new Director();

let soundingRocketBuilder = new SoundingRocketBuilder();
let probe = new Probe();
let soundRocket = director.prepareRocket(soundingRocketBuilder, probe);

let freightRocketBuilder = new FreightRocketBuilder();
let satellite = new Satellite(0, 1200);
let freightRocket = director.prepareRocket(freightRocketBuilder, satellite);

console.info(soundRocket);
console.info(freightRocket);